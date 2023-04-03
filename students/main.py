import os
import getpass

if not os.path.exists('record.txt'):
    with open('record.txt', 'w') as f:
        pass


def register():
    print("========================================")
    print("================Register================")
    print("========================================")

    username = input('Enter username: ')
    username = username.strip()
    if username in open('record.txt').read():
        print('Username already exists')
        exit()
    password = getpass.getpass('Enter password: ')
    password = password.strip()
    confirm_password = getpass.getpass('Confirm password: ')
    confirm_password = confirm_password.strip()
    if password != confirm_password:
        print('Passwords do not match')
        exit()
    with open('record.txt', 'a') as f:
        f.write(f"username:{username}, password:{password}")
        f.write("\n")
    print('Registration successful')


def login():
    print("========================================")
    print("================Login================")
    print("========================================")
    username = input('Enter username: ')
    username = username.strip()
    password = getpass.getpass('Enter password: ')
    password = password.strip()
    with open('record.txt', 'r') as f:
        login_success = False
        for student in f.readlines():
            uname = student.split(',')[0].split(':')[1]
            pword = student.split(',')[1].split(':')[1]
            pword = pword.strip()
            if username == uname and password == pword:
                login_success = True

        if login_success:
            print(f"Welcome {username}")
        else:
            print('Invalid username or password')


question = input("Do you have an account? (y/n): ")
if question == 'y':
    login()
elif question == 'n':
    register()
else:
    print('Invalid input')
    exit()
