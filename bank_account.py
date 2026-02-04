# bank_account.py
# Task 10: Object-Oriented Programming (OOP)
# Simulating a simple Bank Account System

class BankAccount:
    """
    Base class representing a generic bank account
    """

    def __init__(self, account_number, holder_name, balance=0):
        # Encapsulation: private attributes
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

    # Getter methods (encapsulation)
    def get_account_number(self):
        return self.__account_number

    def get_holder_name(self):
        return self.__holder_name

    def get_balance(self):
        return self.__balance

    # Bank operations
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def display_details(self):
        print("\n--- Account Details ---")
        print(f"Account Number : {self.__account_number}")
        print(f"Account Holder : {self.__holder_name}")
        print(f"Balance        : ₹{self.__balance}")


# Inheritance: SavingsAccount inherits BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0, interest_rate=4.0):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    # Polymorphism: overriding method
    def display_details(self):
        super().display_details()
        print(f"Interest Rate  : {self.interest_rate}%")


# Inheritance: CurrentAccount inherits BankAccount
class CurrentAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=10000):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    # Polymorphism: overriding withdraw
    def withdraw(self, amount):
        if amount <= (self.get_balance() + self.overdraft_limit):
            print(f"₹{amount} withdrawn using overdraft facility.")
        else:
            print("Overdraft limit exceeded!")


# Creating multiple objects
if __name__ == "__main__":
    acc1 = SavingsAccount(101, "Sai Charan", 5000)
    acc2 = CurrentAccount(202, "Rahul", 8000)

    acc1.deposit(2000)
    acc1.withdraw(1500)
    acc1.display_details()

    acc2.withdraw(12000)
    acc2.display_details()
