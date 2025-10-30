class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self._pin = pin
        self._balance = balance

    # Validate pin
    def validate_pin(self, entered_pin):
        return entered_pin == self._pin

    # Check Balance
    def check_balance(self):
        print(f"Current Balance: ₹{self._balance}")

    # Deposit Money
    def deposit_money(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ₹{amount}. New Balance: ₹{self._balance}")
        else:
            print("Invalid deposit amount.")

    # Withdraw Money
    def withdraw_money(self, amount):
        if amount > self._balance:
            print("Insufficient balance.")
        elif amount > 0:
            self._balance -= amount
            print(f"Withdrawn ₹{amount}. New Balance: ₹{self._balance}")
        else:
            print("Invalid withdrawal amount.")

    # Change pin
    def change_pin(self, old_pin, new_pin):
        if self.validate_pin(old_pin) and len(new_pin) == 4 and new_pin.isdigit():
            self._pin = new_pin
            print("PIN changed successfully!")
        else:
            print("Invalid PIN change attempt.")


class ATM:
    def __init__(self):
        self.accounts = {}

    # Create account
    def create_account(self):
        account_number = input("Enter Account Number: ")
        pin = input("Set a 4-digit PIN: ")
        if len(pin) == 4 and pin.isdigit():
            self.accounts[account_number] = BankAccount(account_number, pin)
            print("Account created successfully!")
        else:
            print("Invalid PIN. PIN must be a 4-digit number.")

    # Authenticate account
    def authenticate_account(self):
        account_number = input("Enter your Account Number: ")
        pin = input("Enter your 4-digit PIN: ")

        account = self.accounts.get(account_number)
        if account and account.validate_pin(pin):
            print("Authentication successful!\n")
            self.account_menu(account)
        else:
            print("Invalid Account Number or PIN.")

    # Account menu
    def account_menu(self, account):
        while True:
            print("\n===== Account Menu =====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Change PIN")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                account.check_balance()
            elif choice == "2":
                amount = float(input("Enter amount to deposit: "))
                account.deposit_money(amount)
            elif choice == "3":
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw_money(amount)
            elif choice == "4":
                old_pin = input("Enter your old PIN: ")
                new_pin = input("Enter your new 4-digit PIN: ")
                account.change_pin(old_pin, new_pin)
            elif choice == "5":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Try again.")

    # Main menu
    def main_menu(self):
        while True:
            print("\n===== Welcome to Python ATM =====")
            print("1. Create Account")
            print("2. Login to Account")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.authenticate_account()
            elif choice == "3":
                print("Thank you for using Python ATM!")
                break
            else:
                print("Invalid choice. Try again.")


# Run the program
atm = ATM()
atm.main_menu()
