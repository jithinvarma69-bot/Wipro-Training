class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_account_holder_name(self):
        return self.__account_holder_name

    def set_account_holder_name(self, account_holder_name):
        self.__account_holder_name = account_holder_name

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def display_account_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder_name}")
        print(f"Balance: {self.__balance}")


if __name__ == "__main__":
    account1 = BankAccount(account_number="123456789", account_holder_name="John Doe", balance=1000.0)
    account1.display_account_info()
    account1.deposit(500.0)
    account1.withdraw(300.0)
    account1.withdraw(2000.0)
    account1.display_account_info()