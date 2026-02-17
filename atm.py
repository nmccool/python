"""
-----------------------------------------------------------------------
ASSIGNMENT 5B: The ATM (Boss Level)
Name: Neal McCool
Date: 2026-02-16
File: atm.py
-----------------------------------------------------------------------
[X] 1. Initialize balance = 1000.00
[X} 2. Start a WHILE True loop:
        a. Print Menu (1. Balance, 2. Deposit, 3. Withdraw, 4. Transfer, 5. Exit)
        b. Get user choice
        c. MATCH choice:
            case "1": Print formatted balance
            case "2": Get deposit amt -> Validate it is numeric -> Add to balance
            case "3": Get withdraw amt -> Validate it is numeric -> Check for Overdraft -> Subtract
            case "4": Get transfer amt -> Validate it is numeric -> Check for Overdraft -> Subtract
            case "5": Print goodbye -> Break loop
            case _: Print "Invalid Selection"
-----------------------------------------------------------------------
"""
print("-" * 40)

print("Welcome to the Bank of McCool ATM")

balance = float(1000.00)

while True:
    print("\n --- Make a selection ---")
    print("1. Show Account Balance")
    print("2. Make A Deposit")
    print("3. Make A Withdrawal")
    print("4. Transfer Funds")
    print("5. Exit")

    selection = input("\nMake A Selection: ")


    match selection:
        # Balance validation
        case "1":
            print(f"\nYour current balance is: ${balance:,.2f}")
        # Deposit Validation
        case "2":
            deposit = input(f"\nEnter deposit amount: ")
            if deposit.replace(".","", 1).isdigit():
                deposit = float(deposit)
                if deposit <= 0:
                    print(f"Deposit amount must be greater than 0.")    
                else:
                    balance += deposit
                    print(f"\nYour deposit has been accepted. Your new balance is ${balance:,.2f}")
            else:
                print(f"\nPlease enter a valid amount.")
        # Withdrawal Validation
        case "3":
            withdrawal = input(f"\nEnter a withdrawal amount: ")
            if withdrawal.replace(".","", 1).isdigit():
                withdrawal = float(withdrawal)
                if withdrawal <= 0:
                    print(f"Withdrawal amount must be greater than 0.")
                elif withdrawal > balance:
                    print(f"\nInsufficient funds! Your current balance is ${balance:,.2f}. Please select a different amount.")
                else:
                    balance -= withdrawal
                    print(f"\nWithdrawal approved.  Your new balance is ${balance:,.2f}")
            else:
                print(f"\nPlease enter a valid amount.")
        # Transfer validation
        case "4":
            transfer = input(f"Enter transfer amount:")
            if transfer.replace(".","", 1).isdigit():
                transfer = float(transfer)
                if transfer <= 0:
                    print(f"Transfer amount must be greater than 0.")
                elif transfer > balance:
                    print(f"\nInsufficient funds! Your current balance is ${balance:,.2f}. Please select a different amount.")
                else:
                    balance -= transfer
                    print(f"\nTransfer approved.  Your new balance is ${balance:,.2f}")
            else:
                print(f"\nPlease enter a valid amount.")
        #  Exit while true break
        case "5":
            print(f"\nThanks for using the Bank of McCool ATM. Don't forget to take your card!")
            break
        
        case _: print("Invalid selection. Please select 1-5.")
print("-" * 40)
