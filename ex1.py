from abc import ABC, abstractmethod

class BankAccount(ABC):

    def __init__(self, name, balance):
        self.name = name               
        self.__balance = balance       

    @abstractmethod
    def account_type(self):
        pass

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print("Amount Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")

class SavingAccount(BankAccount):

    def __init__(self, name, balance):
        super().__init__(name, balance)  

    def account_type(self):
        print("Account Type: Saving Account")

account = SavingAccount("Krisha", 5000)

account.account_type()
account.deposit(2000)
account.withdraw(1000)
print("Current Balance:", account.get_balance())
