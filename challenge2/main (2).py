class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount} into account {self.__account_number}.")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                print(f"Withdrew ${amount} from account {self.__account_number}.")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0.")

    def display_balance(self):
        print(f"Account {self.__account_number} balance: ${self.__account_balance:.2f}")


# Testing the BankAccount class
if __name__ == "__main__":
    # Create a new bank account
    account1 = BankAccount("12345", "John Doe", 1000.0)

    # Display the initial balance
    account1.display_balance()

    # Deposit money into the account
    account1.deposit(500.0)

    # Display the updated balance
    account1.display_balance()

    # Withdraw money from the account
    account1.withdraw(200.0)

    # Display the final balance
    account1.display_balance()
