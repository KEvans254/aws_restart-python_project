#!/usr/bin/env python3
import time
import json
from datetime import datetime
from datetime import date
import os.path

def json_to_dict():
    global clients
    with open('clients.json') as json_file:
        clients = json.load(json_file)


json_to_dict()

count = (clients.__len__())

def update_clients():
    f = open("clients.json", "w")
    json.dump(clients, f)
    f.close()


def unblock_menu():
    menu_choice = input("""WELCOME TO THE ACCOUNT UNBLOCK MENU.
    What would you like to do today?
    
    1   Check if account is blocked.
    2   Unblock account.
    3   Check number of failed attempts.
    Enter choice: """)
    if menu_choice == "1":
        check_if_blocked()
    elif menu_choice == "2":
        unblock()
    elif menu_choice == "3":
        check_failed_attempts()
    else:
        print("Please choose a valid option.")
        time.sleep(2)
        unblock_menu()


def check_if_blocked():
    user_match = False
    global user_name
    user_name = input("\nEnter username of account to check block status: ")
    string = user_name
    global counter
    global login_time
    global login_day
    now = datetime.now()
    login_time = now.strftime("%H:%M:%S")
    today = date.today()
    login_day = today.strftime("%B %d, %Y")
    counter = 0
    while counter < count:
        if clients[str(counter)]['username'] == user_name:
            user_match = True
            if clients[str(counter)]['blocked'] == True:
                if string[-1] == "s":
                    print(f"{user_name}' account has been BLOCKED.\n")
                else:
                    print(f"{user_name}'s account has been BLOCKED.\n")
            else:
                if string[-1] == "s":
                    print(f"{user_name}' account has NOT yet been BLOCKED.\n")
                else:
                    print(f"{user_name}'s account has NOT yet been BLOCKED.\n")
                time.sleep(3)
                unblock_menu()
        counter += 1
    if not user_match:
        print("Username not found. Please try again.")
        time.sleep(3)
        unblock_menu()


def check_failed_attempts():
    user_match = False
    global user_name
    user_name = input("\nEnter username of account to check number of failed attempts: ")
    global counter
    global login_time
    global login_day
    now = datetime.now()
    login_time = now.strftime("%H:%M:%S")
    today = date.today()
    login_day = today.strftime("%B %d, %Y")
    counter = 0
    while counter < count:
        if clients[str(counter)]['username'] == user_name:
            user_match = True
            f = open(f"{user_name}_attempts.txt", "r")
            attempts = int(f.read())
            print(f"""
            {user_name} has {attempts} failed login attempts.
            The user has {3-attempts} left before the account gets blocked.\n
            """)
            unblock_menu()
        counter += 1
    if not user_match:
        print("Username not found. Please try again.")
        time.sleep(3)
        unblock_menu()


def unblock():
    user_match = False
    global user_name
    user_name = input("\nEnter username of account to unblock: ")
    global counter
    global login_time
    global login_day
    now = datetime.now()
    login_time = now.strftime("%H:%M:%S")
    today = date.today()
    login_day = today.strftime("%B %d, %Y")
    counter = 0
    while counter < count:
        if clients[str(counter)]['username'] == user_name:
            user_match = True
            file_exists = os.path.exists(f'{user_name}_attempts.txt')
            if file_exists:
                f = open(f"{user_name}_attempts.txt", "w")
                f.write("0")
                f.close()
            else:
                print("Account is missing 'attempts.txt' file.")
                time.sleep(3)
                unblock_menu()
            if clients[str(counter)]['blocked'] == True:
                clients[str(counter)]['blocked'] = False
                update_clients()
                print(f"{user_name}'s account has successfully been unblocked.\n")
                unblock_log()
            else:
                print("Account has not yet been blocked.\n")
                time.sleep(3)
                unblock_menu()
        counter += 1
    if not user_match:
        print("Username not found. Please try again.")
        time.sleep(3)
        unblock_menu()


def unblock_log():
    log = open(f"{user_name}_log.txt", "a+")
    text = [f"\n\nOPERATION: Account successfully UNBLOCKED.\n",
            f"   User: {user_name}\n", f"  Unblock day: {login_day} \n", f"  Unblock time: {login_time} \n"]
    log.writelines(text)
    log.close()

unblock_menu()