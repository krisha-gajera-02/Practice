class InsufficientBalanceError(Exception):
    pass

try:
    balance = 5000

    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Amount must be positive")

    if amount > balance:
        raise InsufficientBalanceError("Not enough balance")

    balance -= amount

except ValueError as ve:
    print("Value Error:", ve)

except InsufficientBalanceError as ibe:
    print("Balance Error:", ibe)

except Exception as e:
    print("Unexpected Error:", e)

else:
    print("Withdrawal successful")
    print("Remaining balance:", balance)

finally:
    print("Transaction completed. Thank you!")
