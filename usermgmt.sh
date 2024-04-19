#!/bin/bash

# Check if the current user is an administrator
if [ $(id -u) -ne 0 ]; then
    echo "You must be root to run this script."
    exit 1
fi

# Execute the Python script with the provided arguments
python3 usermgmt.py "$@"




