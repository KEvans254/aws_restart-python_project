#!/usr/bin/env python3
import time
import json
from datetime import datetime
from datetime import date


# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# User database dictionary


def update_clients():
    f = open("clients.json", "w")
    json.dump(clients, f)
    f.close()


def json_to_dict():
    global clients
    with open('clients.json') as json_file:
        clients = json.load(json_file)


json_to_dict()

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
            user_password = int(input("Enter pin: "))
            break
        except ValueError:
            print("Ensure the pin entered is a number.")
            time.sleep(3)
            print(50 * "\n")
            onboard()
    global counter
    global login_time
    global login_day
    counter = 0
    while counter < count:
        if clients[str(counter)]['username'] == user_name and clients[str(counter)]['pin'] == user_password:
            print("Successful login!")
            user_match = True
            now = datetime.now()
            login_time = now.strftime("%H:%M:%S")
            today = date.today()
            login_day = today.strftime("%B %d, %Y")
            login_log()
            menu()
            break
        counter += 1
    if not user_match:
        print("Incorrect details entered. Please try again.")
        time.sleep(3)
        print(50 * "\n")
        onboard()


def menu():
    print("""
    Login day: {} and login time: {}
    WELCOME, {}. This is the MAIN MENU. What would you like to do today?
    1   Check account balance.
    2   Withdraw money
    3   Deposit money
    4   Account Manager
    5   Quit  
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
        account()
    elif menu_choice == 5:
        exit()
    else:
        print("Please select a valid choice.")
        menu()


def balance():
    global KSHbala
    global USDbala
    KSHbala = clients[str(counter)]['balance']['KSh']
    USDbala = clients[str(counter)]['balance']['USD']
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
    if ksh_wamount > int(clients[str(counter)]['balance']['KSh']):
        print("Amount exceeds your KSH account balance. Please top up first.")
        time.sleep(3)
        menu()
    if ksh_wamount < 5:
        print("Minimum withdrawal amount is 5 shillings.")
        time.sleep(3)
        withdrawal()
    ksh_bal_calc = int(clients[str(counter)]['balance']['KSh']) - ksh_wamount
    clients[str(counter)]['balance']['KSh'] = str(ksh_bal_calc)
    update_clients()
    withdrawal_log()
    print("{}, you have successfully withdrawn {} shillings from your KSH account.".format(user_name, ksh_wamount))
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
    if usd_wamount > int(clients[str(counter)]['balance']['USD']):
        print("Amount exceeds your USD account balance. Please top up first.")
        time.sleep(3)
        menu()
    if usd_wamount < 1:
        print("Minimum withdrawal amount is 1 USD.")
        time.sleep(3)
        withdrawal()
    usd_bal_calc = int(clients[str(counter)]['balance']['USD']) - usd_wamount
    clients[str(counter)]['balance']['USD'] = str(usd_bal_calc)
    update_clients()
    withdrawal_log()
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
    ksh_bal_calc = int(clients[str(counter)]['balance']['KSh']) + ksh_damount
    clients[str(counter)]['balance']['KSh'] = str(ksh_bal_calc)
    update_clients()
    deposit_log()
    print("{}, you have successfully deposited {} shillings to your KSH account.".format(user_name, ksh_damount))
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
    usd_bal_calc = int(clients[str(counter)]['balance']['USD']) + usd_damount
    clients[str(counter)]['balance']['USD'] = str(usd_bal_calc)
    update_clients()
    deposit_log()
    print("{}, you have successfully deposited {} dollars to your USD account.".format(user_name, usd_damount))
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


def login_log():
    log = open(f"{user_name}_log.txt", "a+")
    text = [f"\n\nOPERATION: Successful login. \n", f"   User: {user_name}\n", f"  Login day: {login_day} \n",
            f"  Login time: {login_time} \n"]
    log.writelines(text)
    log.close()


def pinchange_log():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    log = open(f"{user_name}_log.txt", "a+")
    text = [f"\n\nOPERATION: PIN CHANGE. \n", f"   User: {user_name}\n", f"  Day: {d2} \n",
            f"  Time: {current_time} \n"]
    log.writelines(text)
    log.close()


def logout_log():
    log = open(f"{user_name}_log.txt", "a+")
    text = [f"OPERATION: Successful logout. \n", f"   User: {user_name}\n", f"  Logout day: {logout_day} \n",
            f"  Logout time: {logout_time} \n"]
    log.writelines(text)
    log.close()


def logaccess():
    log_access = open(f"{user_name}_log.txt", "r")
    print(log_access.read())
    print()
    log_access.close()
    time.sleep(3)
    account()


def transactionlogaccess():
    trlogaccess = open(f"{user_name}_transaction_log.txt", "r")
    print(trlogaccess.read())
    print()
    trlogaccess.close()
    time.sleep(3)
    account()


def withdrawal_log():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    if w_account == 1:
        account = "KSH"
        amount = ksh_wamount
    else:
        account = "USD"
        amount = usd_wamount
    log = open(f"{user_name}_transaction_log.txt", "a+")
    text = [f"\n\nOPERATION: Withdrawal. \n", f"   User: {user_name}\n", f"  Day: {d2} \n",
            f"  Time: {current_time} \n", f"   Account: {account}\n", f"   Amount: {amount}\n"]
    log.writelines(text)
    log.close()


def deposit_log():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    if d_account == 1:
        account = "KSH"
        amount = ksh_damount
    else:
        account = "USD"
        amount = usd_damount
    log = open(f"{user_name}_transaction_log.txt", "a+")
    text = [f"\n\nOPERATION: Deposit. \n", f"   User: {user_name}\n", f"  Day: {d2} \n",
            f"  Time: {current_time} \n", f"   Account: {account}\n", f"   Amount: {amount}\n"]
    log.writelines(text)
    log.close()


def account():
    account_menu_choice = input(f"""
    {user_name}, welcome to your account management menu.
    What would you like to do now?
    1   Change pin
    2   View account log
    3   View transaction log
    4   Go back to main menu
    Enter choice: 
    """)
    if account_menu_choice == "1":
        pin_change()
    elif account_menu_choice == "2":
        logaccess()
    elif account_menu_choice == "3":
        transactionlogaccess()
    elif account_menu_choice == "4":
        menu()
    else:
        print("Please select a valid option.")
        account()


def pin_change():
    while True:
        try:
            old_pin = int(input("Enter old pin: "))
            break
        except ValueError:
            print("Ensure the pin entered is a number.")
            time.sleep(2)
            account()
    if old_pin == user_password:
        new_pin1 = int(input("Enter new pin: "))
        new_pin2 = int(input("Reconfirm new pin: "))
        if new_pin1 != new_pin2:
            print("Pins do not match. Try again.")
            time.sleep(2)
            account()
        elif new_pin1 == old_pin:
            print("New pin cannot be same as old pin.")
            time.sleep(2)
            account()
        else:
            clients[str(counter)]['pin'] = new_pin1
            update_clients()
            pinchange_log()
            print("""
                            PIN CHANGED SUCCESSFULLY. 
                        YOU WILL HAVE TO LOG BACK IN WITH THE NEW PIN.

                            *** LOGGING OUT ***
                            *** PLEASE WAIT ... ***
                            """)
            time.sleep(3)
            print(20 * "\n")
            onboard()
    else:
        print("Incorrect details entered. Please try again.")
        time.sleep(1)
        account()


def exit():
    exit_confirm = input("""
    Are you sure you want to log out, {}? 
    1   YES
    2   NO
    Enter choice: """.format(user_name))
    if exit_confirm.upper() == "YES" or exit_confirm.upper() == "1":
        global logout_day
        global logout_time
        now = datetime.now()
        logout_time = now.strftime("%H:%M:%S")
        today = date.today()
        logout_day = today.strftime("%B %d, %Y")
        logout_log()
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
