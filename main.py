#!/usr/bin/env python3
import time
from datetime import datetime
from datetime import date

# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# User database dictionary
clients = {
    0: {
        "username": "trial",
        "pin": 0000,
        "balance": {"KSh": 140, "USD": 0}
    },
    1: {
        "username": "evans",
        "pin": 1111,
        "balance": {"KSh": 1500, "USD": 10}
    }
}
# print(clients[1]['username'])
count = (clients.__len__())


def onboard():
    print('''
    WELCOME TO ALPHA BANK ATM SYSTEM.
    PLEASE LOG IN TO CONTINUE.
    ''')
    login()


def login():
    user_match = False
    while True:
        try:
            global user_name
            user_name = input("\nEnter username: ")
            break
        except ValueError:
            print("Username should be a string.")
            onboard()
    while True:
        try:
            global user_password
            user_password = int(input("Enter password: "))
            break
        except ValueError:
            print("Ensure the password entered is a number.")
            time.sleep(1)
            print(50 * "\n")
            onboard()
    global counter
    global login_time
    global login_day
    counter = 0
    while counter < count:
        if clients[counter]['username'] == user_name and clients[counter]['pin'] == user_password:
            print("Successful login!")
            user_match = True
            now = datetime.now()
            login_time = now.strftime("%H:%M:%S")
            today = date.today()
            login_day = today.strftime("%B %d, %Y")
            menu()
            break
        counter += 1
    if user_match != True:
        print("Incorrect details entered. Please try again.")
        time.sleep(1)
        print(50 * "\n")
        onboard()


def menu():
    print("""
    Last login day: {} and last login time: {}
    WELCOME, {}. This is the MAIN MENU. What would you like to do today?
    1   Check account balance.
    2   Withdraw money
    3   Deposit money
    4   Quit  
    """.format(login_day, login_time, user_name))
    while True:
        try:
            global menu_choice
            menu_choice = 0
            menu_choice = int(input("Enter choice: "))
            break
        except ValueError or NameError:
            print("The choice should be an integer.")
            menu()
    if menu_choice == 1:
        balance()
    elif menu_choice == 2:
        withdrawal()
    elif menu_choice == 3:
        deposit()
    elif menu_choice == 4:
        exit()
    else:
        print("Please select a valid choice.")
        menu()

def balance():
    global KSHbala
    global USDbala
    KSHbala = clients[counter]['balance']['KSh']
    USDbala = clients[counter]['balance']['USD']
    print("""
    Dear {}, you have {} shillings in your KSh. account
    and {} dollars in your USD account.
    """.format(user_name, KSHbala, USDbala))
    time.sleep(2)
    balancereceipt()

def balancereceipt():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    d2 = today.strftime("%B %d, %Y")

    balreceiptchoice = input("""
    {}, do you need a receipt showing your balance? 
    1   YES
    2   NO
    Enter choice: """.format(user_name))
    if balreceiptchoice.upper() == "YES" or balreceiptchoice.upper() == "1":
        print("""
                ******************************************************
                *             ALPHA BANK ATM SYSTEM
                *       ACCOUNT BALANCE RECEIPT
                *   Date: {}                               
                *   Time: {}
                *   User: {}
                *   Balance: KSh {}
                *            USD {}
                *********************END OF RECEIPT*******************
                ******************************************************
                """.format(d2, current_time, user_name, KSHbala, USDbala))
        time.sleep(3)
        menu()
    elif balreceiptchoice.upper() == "NO" or balreceiptchoice.upper() == "2":
        menu()
    else:
        print("Please select a valid option.")
        balancereceipt()

def withdrawal():
    global w_account
    while True:
        try:
            w_account = int(input("""
    {}, which account would you like to withdraw from?
    1   KSH
    2   USD
    3   EXIT to main menu
    Enter choice: """.format(user_name)))
            if w_account == 1:
                kshwithdrawal()
            elif w_account == 2:
                usdwithdrawal()
                pass
            elif w_account == 3:
                menu()
            else:
                print("Please select a valid option.")
                withdrawal()
            break
        except ValueError:
            print("The choice should be an integer.")
            withdrawal()


def kshwithdrawal():
    global ksh_wamount
    while True:
        try:
            ksh_wamount = int(input("\n    Enter amount to withdraw from KSH account: "))
            break
        except ValueError:
            print("The amount should be an integer.")
            kshwithdrawal()
    if ksh_wamount > int(clients[counter]['balance']['KSh']):
        print("Amount exceeds your KSH account balance. Please top up first.")
        time.sleep(3)
        menu()
    if ksh_wamount < 5:
        print("Minimum withdrawal amount is 5 shillings.")
        time.sleep(3)
        withdrawal()
    ksh_bal_calc = int(clients[counter]['balance']['KSh']) - ksh_wamount
    clients[counter]['balance']['KSh'] = str(ksh_bal_calc)
    print("{}, you have successfully withdrawn {} shillings from your KSH account.".format(user_name,ksh_wamount))
    time.sleep(3)
    ksh_withdrawal_receipt()

def usdwithdrawal():
    global usd_wamount
    while True:
        try:
            usd_wamount = int(input("\n    Enter amount to withdraw from USD account: "))
            break
        except ValueError:
            print("The amount should be an integer.")
            kshwithdrawal()
    if usd_wamount > int(clients[counter]['balance']['USD']):
        print("Amount exceeds your USD account balance. Please top up first.")
        time.sleep(3)
        menu()
    if usd_wamount < 1:
        print("Minimum withdrawal amount is 1 USD.")
        time.sleep(3)
        withdrawal()
    usd_bal_calc = int(clients[counter]['balance']['USD']) - usd_wamount
    clients[counter]['balance']['USD'] = str(usd_bal_calc)
    print("{}, you have successfully withdrawn {} dollars from your USD account.".format(user_name, usd_wamount))
    time.sleep(3)
    usd_withdrawal_receipt()

def ksh_withdrawal_receipt():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    d2 = today.strftime("%B %d, %Y")

    kshwreceiptchoice = input("""
    {}, do you need a receipt for your transaction? 
    1   YES
    2   NO
    Enter choice: """.format(user_name))
    if kshwreceiptchoice.upper() == "YES" or kshwreceiptchoice.upper() == "1":
        print("""
                ******************************************************
                *             ALPHA BANK ATM SYSTEM
                *       WITHDRAWAL RECEIPT
                *   Date: {}                               
                *   Time: {}
                *   User: {}
                *   Account: KSH
                *   Amount: {} shillings
                *********************END OF RECEIPT*******************
                ******************************************************
                """.format(d2, current_time, user_name, ksh_wamount))
        time.sleep(3)
        after_withdrawal()
    elif kshwreceiptchoice.upper() == "NO" or kshwreceiptchoice.upper() == "2":
        after_withdrawal()
    else:
        print("Please select a valid option.")
        ksh_withdrawal_receipt()

def usd_withdrawal_receipt():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    d2 = today.strftime("%B %d, %Y")

    usdwreceiptchoice = input("""
    {}, do you need a receipt for your transaction? 
    1   YES
    2   NO
    Enter choice: """.format(user_name))
    if usdwreceiptchoice.upper() == "YES" or usdwreceiptchoice.upper() == "1":
        print("""
                ******************************************************
                *             ALPHA BANK ATM SYSTEM
                *       WITHDRAWAL RECEIPT
                *   Date: {}                               
                *   Time: {}
                *   User: {}
                *   Account: USD
                *   Amount: {} shillings
                *********************END OF RECEIPT*******************
                ******************************************************
                """.format(d2, current_time, user_name, usd_wamount))
        time.sleep(3)
        after_withdrawal()
    elif usdwreceiptchoice.upper() == "NO" or usdwreceiptchoice.upper() == "2":
        after_withdrawal()
    else:
        print("Please select a valid option.")
        usd_withdrawal_receipt()

def after_withdrawal():
    another_withdrawal = input("""
    {}, would you like to make another withdrawal transaction?
    1   YES
    2   NO
    Enter choice: """.format(user_name))
    if another_withdrawal.upper() == "YES" or another_withdrawal == "1":
        withdrawal()
    elif another_withdrawal.upper() == "NO" or another_withdrawal == "2":
        menu()
    else:
        print("Please select a valid option.")
        after_withdrawal()

def deposit():
    global d_account
    while True:
        try:
            d_account = int(input("""
    {}, which account would you like to deposit to?
    1   KSH
    2   USD
    3   EXIT to main menu
    Enter choice: """.format(user_name)))
            if d_account == 1:
                kshdeposit()
            elif d_account == 2:
                usddeposit()
                pass
            elif d_account == 3:
                menu()
            else:
                print("Please select a valid option.")
                deposit()
            break
        except ValueError:
            print("The choice should be an integer.")
            deposit()


def kshdeposit():
    global ksh_damount
    while True:
        try:
            ksh_damount = int(input("Enter amount to deposit to KSH account: "))
            break
        except ValueError:
            print("The amount should be an integer.")
            kshdeposit()
    if ksh_damount < 0:
        print("Minimum deposit amount is 5 shillings.")
        time.sleep(3)
        deposit()
    ksh_bal_calc = int(clients[counter]['balance']['KSh']) + ksh_damount
    clients[counter]['balance']['KSh'] = str(ksh_bal_calc)
    print("{}, you have successfully deposited {} shillings to your KSH account.".format(user_name,ksh_damount))
    time.sleep(3)
    ksh_deposit_receipt()

def usddeposit():
    global usd_damount
    while True:
        try:
            usd_damount = int(input("Enter amount to deposit to USD account: "))
            break
        except ValueError:
            print("The amount should be an integer.")
            kshwithdrawal()
    if usd_damount < 0:
        print("Minimum deposit amount is 1 USD.")
        time.sleep(3)
        deposit()
    usd_bal_calc = int(clients[counter]['balance']['USD']) + usd_damount
    clients[counter]['balance']['USD'] = str(usd_bal_calc)
    print("{}, you have successfully deposuted {} dollars to your USD account.".format(user_name, usd_damount))
    time.sleep(3)
    usd_deposit_receipt()

def ksh_deposit_receipt():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    d2 = today.strftime("%B %d, %Y")

    kshdreceiptchoice = input("""
    {}, do you need a receipt for your transaction? 
    1   YES
    2   NO
    Enter choice: """.format(user_name))
    if kshdreceiptchoice.upper() == "YES" or kshdreceiptchoice.upper() == "1":
        print("""
                ******************************************************
                *             ALPHA BANK ATM SYSTEM
                *       DEPOSIT RECEIPT
                *   Date: {}                               
                *   Time: {}
                *   User: {}
                *   Account: KSH
                *   Amount: {} shillings
                *********************END OF RECEIPT*******************
                ******************************************************
                """.format(d2, current_time, user_name, ksh_damount))
        time.sleep(3)
        after_deposit()
    elif kshdreceiptchoice.upper() == "NO" or kshdreceiptchoice.upper() == "2":
        after_deposit()
    else:
        print("Please select a valid option.")
        ksh_deposit_receipt()

def usd_deposit_receipt():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    d2 = today.strftime("%B %d, %Y")

    usddreceiptchoice = input("""
    {}, do you need a receipt for your transaction? 
    1   YES
    2   NO
    Enter choice: """.format(user_name))
    if usddreceiptchoice.upper() == "YES" or usddreceiptchoice.upper() == "1":
        print("""
                ******************************************************
                *             ALPHA BANK ATM SYSTEM
                *       DEPOSIT RECEIPT
                *   Date: {}                               
                *   Time: {}
                *   User: {}
                *   Account: USD
                *   Amount: {} shillings
                *********************END OF RECEIPT*******************
                ******************************************************
                """.format(d2, current_time, user_name, usd_damount))
        time.sleep(3)
        after_deposit()
    elif usddreceiptchoice.upper() == "NO" or usddreceiptchoice.upper() == "2":
        after_deposit()
    else:
        print("Please select a valid option.")
        balancereceipt()

def after_deposit():
    another_deposit = input("""
    {}, would you like to make another deposit transaction?
    1   YES
    2   NO
    Enter choice: """.format(user_name))
    if another_deposit.upper() == "YES" or another_deposit == "1":
        deposit()
    elif another_deposit.upper() == "NO" or another_deposit == "2":
        menu()
    else:
        print("Please select a valid option.")
        after_deposit()

def exit():
    exit_confirm = input("""
    Are you sure you want to log out, {}? 
    1   YES
    2   NO
    Enter choice: """.format(user_name))
    if exit_confirm.upper() == "YES" or exit_confirm.upper() == "1":
        print("""
                *** LOGGING OUT ***
                *** PLEASE WAIT ... ***
                """)
        time.sleep(3)
        print(50 * "\n")
        onboard()
    elif exit_confirm.upper() == "NO" or exit_confirm.upper() == "2":
        menu()
    else:
        print("Please select a valid option.")
        exit()

onboard()

