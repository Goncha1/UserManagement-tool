# UserManagement-tool
A tool for managing users for administrators
 User Management and Login Tools

## Overview

This repository contains two command-line tools written in Python: `usermgmt` for user management operations and `login` for user login functionality.

## User Management Tool (`usermgmt.sh` and `usermgmt.py`)

### Functionalities

1. Adding a new username (`add` operation).
2. Changing the password of an existing username (`passwd` operation).
3. Forcing a password change when the user logs in (`forcepass` operation).
4. Removing an existing username (`del` operation).

### Protection Measures

- **Adding a new username (`add` operation):**
  - The `add` operation requires administrator privileges to execute. This ensures that only authorized users can create new user accounts.
  - The script verifies the password entered by the administrator, ensuring that only authenticated administrators can perform this action.

- **Changing the password (`passwd` operation):**
  - The `passwd` operation can only be performed by users who have authenticated themselves with their current password. This prevents unauthorized password changes.
  - Administrators can force password changes for users if necessary, but this action also requires the administrator's password for verification.

- **Forcing a password change (`forcepass` operation):**
  - The `forcepass` operation is restricted to administrators only. Regular users cannot force password changes.
  - Administrators must authenticate themselves with their password to force a password change for a user.
  - After a successful login, users are prompted to change their password if an administrator has forced a password change.

- **Removing a user (`del` operation):**
  - The `del` operation is limited to administrators to prevent unauthorized deletion of user accounts.
  - Administrators must authenticate themselves with their password to delete a user account.

### Usage

To use the `usermgmt` tool, run the `usermgmt.sh` script with the desired operation and username as arguments. For example:
```
./usermgmt.sh add alice
./usermgmt.sh passwd alice
./usermgmt.sh forcepass alice
./usermgmt.sh del alice
```

## Login Tool (`login.py` and `login.sh`)

### Functionalities

1. Entering the username and password securely.
2. Starting a specified command (e.g., `ls`) after a successful login.

### Protection Measures

- User credentials (username and password) are securely entered using the `getpass` module, ensuring that passwords are not visible during input.
- After a successful login, users are prompted to change their password if an administrator has forced a password change.

### Usage

To use the `login` tool, run the `login.py` script and enter the username and password when prompted. For example:
```
python login.py
```
Or
```
./login.sh

```


## User Data File (`user_data.json`)

Both tools use a JSON file (`user_data.json`) to store user information such as usernames, hashed passwords, and flags for password change requirements.

### User Data Structure

```json
{
  "username": {
    "password": "hashed_password",
    "force_change": false
  }
}
```

- `password`: Hashed password for the user.
- `force_change`: Indicates if the user must change their password during the next login.

## Requirements

- Python 3.x
- hashlib library (for password hashing)
- subprocess library (for executing shell commands)

## Notes

- The `usermgmt` tool requires administrator privileges to run (`root` or `sudo` access).
- Ensure that the `user_data.json` file is properly formatted with the necessary user information.
