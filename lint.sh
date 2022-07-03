#!/bin/sh

set -o errexit

exit_handler() {
    if [ $? -ne 0 ]; then
        echo "Failure" >&2
    fi
}

get_roles_dir() {
    local cache_key
    local cache_dir

    # See:
    # https://github.com/ansible/ansible-compat/blob/1d53bc95b95485710c179d6186deebf25aa930bc/src/ansible_compat/prerun.py
    cache_key=$(printf $(basename "${PWD}") | sha256sum -b - | head -c 6)
    cache_dir="${HOME}/.cache/ansible-compat/${cache_key}"

    echo "${cache_dir}/roles"
}

ansiblelint_wrapper() {
    local role_name=$(basename "${PWD}")
    local exit_status
    local mock_path

    # Set up role mock. A workaround to bypass the following error:
    # internal-error: the role '<...>' was not found in <...>
    # See https://github.com/ansible/ansible-lint/issues/1329
    mock_path="$(get_roles_dir)/${role_name}"
    mkdir -p "${mock_path}"

    set +o errexit

    ansible-lint
    exit_status=$?

    set -o errexit

    # Tear down mock. Molecule imports roles from the same chache directory.
    rm -r -f "${mock_path}"

    if [ ${exit_status} -ne 0 ]; then
        exit 1
    fi
}

trap exit_handler EXIT

echo "Running ansible-lint..."
ansiblelint_wrapper

echo "Success"
