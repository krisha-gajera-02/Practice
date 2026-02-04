import time

def login_required(func):
    def wrapper(*args, **kwargs):
        print("Checking login...")
        return func(*args, **kwargs)
    return wrapper

def timer(unit):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"Time taken: {round(end - start, 4)} {unit}")
            return result
        return wrapper
    return decorator

class Bank:

    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        self._balance = amount

    @staticmethod
    def bank_info():
        print("Welcome to Python Bank")

    @classmethod
    def rules(cls):
        print("Minimum balance must be maintained")

@login_required
@timer("seconds")
def withdraw(amount):
    print("Withdrawing:", amount)
    time.sleep(1)
    return amount

Bank.bank_info()
Bank.rules()

print("Balance:", Bank(5000).balance)

withdraw(1000)
