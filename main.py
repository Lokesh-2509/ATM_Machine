class InsufficientFundsException(Exception):
    pass
class InvalidAmountException(Exception):
    pass
class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountException("Invalid amount. Amount must be greater than zero.")
        self.balance += amount
        print(f"Deposit of {amount} New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountException("Invalid amount. Amount must be greater than zero.")
        if amount > self.balance:
            raise InsufficientFundsException("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrawal of {amount} New balance: {self.balance}")
atm = ATM(5000)
while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    choice = int(input("Select an option: "))
    if choice == 1:
        amount = float(input("deposit amount: "))
        try:
            atm.deposit(amount)
        except InvalidAmountException as e:
            print(f"Invalid amount: {str(e)}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    elif choice == 2:
        amount = float(input("withdrawal amount: "))
        try:
            atm.withdraw(amount)
        except InvalidAmountException as e:
            print(f"Invalid amount: {str(e)}")
        except InsufficientFundsException as e:
            print(f"Insufficient funds: {str(e)}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    elif choice == 3:
        break
    print()
print("Exiting the ATM program.")
