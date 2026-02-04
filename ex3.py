import threading
import time

balance = 1000

lock = threading.Lock()

def withdraw(amount):

    global balance
    
    print(f"{threading.current_thread().name} started")

    with lock:   
        if balance >= amount:
            print(f"{threading.current_thread().name} withdrawing {amount}")
            time.sleep(1)   
            balance -= amount
            print(f"Remaining Balance: {balance}")
        else:
            print("Insufficient Balance")

    print(f"{threading.current_thread().name} finished\n")

t1 = threading.Thread(target=withdraw, args=(700,), name="Thread-1")
t2 = threading.Thread(target=withdraw, args=(500,), name="Thread-2")

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Balance:", balance)
