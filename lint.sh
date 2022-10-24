#!/bin/sh

set -o nounset

echo "Running ansible-lint..."
ANSIBLE_ROLES_PATH="${MOLECULE_EPHEMERAL_DIRECTORY}/roles" \
ANSIBLE_COLLECTIONS_PATH="${MOLECULE_EPHEMERAL_DIRECTORY}/collections" \
ansible-lint \
    "${MOLECULE_PROJECT_DIRECTORY}" \
    "${MOLECULE_SCENARIO_DIRECTORY}"
if [ $? -ne 0 ]; then
    echo "Error: ansible-lint failed" >&2
    exit 1
fi

echo "Success"
