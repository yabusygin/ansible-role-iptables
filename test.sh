#!/bin/sh

platforms="geerlingguy/docker-debian11-ansible:latest"

for image in ${platforms}; do
    echo "Running Molecule tests for '${image}'..."
    TEST_IMAGE="${image}" molecule test --all
    if [ $? -ne 0 ]; then
        echo "Error: Molecule test failed (platform: ${image})" >&2
        exit 1
    fi
done

echo "Success: all tests are passed"
