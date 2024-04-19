import json
import hashlib
import getpass
import subprocess

def load_users():
    try:
        with open('user_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open('user_data.json', 'w') as file:
        json.dump(users, file)

def login(username):
    users = load_users()
    if username not in users:
        print("Username or password incorrect.")
        return

    password_attempts = 3
    while password_attempts > 0:
        password = getpass.getpass("Password: ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if users[username]['password'] == hashed_password:
            if users[username].get('force_change'):
                print("Administrator has requested a password change.")
                new_password = getpass.getpass("New password: ")
                repeat_password = getpass.getpass("Repeat new password: ")
                if new_password == repeat_password:
                    hashed_new_password = hashlib.sha256(new_password.encode()).hexdigest()
                    users[username]['password'] = hashed_new_password
                    users[username]['force_change'] = False
                    save_users(users)
                    print("Password changed successfully.")
                else:
                    print("New passwords do not match. Please contact the administrator.")
                    break

            print("Login successful.")
            subprocess.run(["ls"], shell=True)  
            break
        else:
            password_attempts -= 1
            if password_attempts == 0:
                print("Maximum login attempts reached. Exiting.")
            else:
                print("Username or password incorrect.")

# Example Usage
if __name__ == "__main__":
    username = input("Username: ")
    login(username)
