def atm_transactions(transactions):
    print("ATM Transaction Started")

    for t in transactions:
        try:
            if t < 0:
                raise ValueError("Invalid transaction amount")
            yield t
        except ValueError as e:
            print("Error:", e)

    print("ATM Transaction Ended")


# ---------- Using Generator ----------
transactions = [500, 1000, -200, 700]

gen = atm_transactions(transactions)

# next()
print("First Transaction:", next(gen))

# for loop iteration
for amount in gen:
    print("Processing Amount:", amount)
