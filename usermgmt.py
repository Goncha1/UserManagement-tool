import json
import hashlib
import sys
import getpass

def load_data():
    try:
        with open('user_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open('user_data.json', 'w') as file:
        json.dump(data, file)

def add_user(username, password):
    data = load_data()
    if username in data:
        print(f"User add failed. Username '{username}' already exists.")
    else:
        repeat_password = getpass.getpass("Repeat Password: ")
        if password != repeat_password:
            print("User add failed. Password mismatch.")
        else:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            data[username] = {'password': hashed_password, 'force_change': False}
            save_data(data)
            print(f"User '{username}' successfully added.")

def change_password(username, new_password):
    data = load_data()
    if username not in data:
        print(f"Password change failed. Username '{username}' does not exist.")
    else:
        repeat_password = getpass.getpass("Repeat Password: ")
        if new_password != repeat_password:
            print("Password change failed. Password mismatch.")
        else:
            hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
            data[username]['password'] = hashed_password
            save_data(data)
            print("Password change successful.")

def force_password_change(username):
    data = load_data()
    if username not in data:
        print(f"User '{username}' not found.")
    else:
        data[username]['force_change'] = True
        save_data(data)
        print(f"User '{username}' will be requested to change password on next login.")

def delete_user(username):
    data = load_data()
    if username not in data:
        print(f"User '{username}' not found.")
    else:
        del data[username]
        save_data(data)
        print(f"User '{username}' successfully removed.")

# Check if the script is being called from the command line
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python usermgmt.py <command> <username>")
        sys.exit(1)

    command = sys.argv[1]
    username = sys.argv[2]

    if command == "add":
        password = getpass.getpass("Password: ")
        add_user(username, password)
    elif command == "passwd":
        new_password = getpass.getpass("New Password: ")
        change_password(username, new_password)
    elif command == "forcepass":
        force_password_change(username)
    elif command == "del":
        delete_user(username)
    else:
        print("Invalid command.")

