import asyncio

balance = 1000

lock = asyncio.Lock()

async def withdraw(name, amount):
    global balance

    print(f"{name} started withdrawal")

    async with lock: 
        if balance >= amount:
            print(f"{name} withdrawing {amount}")
            await asyncio.sleep(1)   
            balance -= amount
            print(f"{name} remaining balance: {balance}")
        else:
            print(f"{name} insufficient balance")

    print(f"{name} finished\n")

async def main():

    t1 = asyncio.create_task(withdraw("User-1", 700))
    t2 = asyncio.create_task(withdraw("User-2", 500))

    await asyncio.gather(t1, t2)

    print("Final Balance:", balance)

asyncio.run(main())
