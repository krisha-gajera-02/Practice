# Collections Library

from collections import Counter, defaultdict, OrderedDict, deque, namedtuple, ChainMap

def collections_demo():

    print("1. Counter")
    data = ["apple", "banana", "apple", "orange", "banana", "apple"]
    counter = Counter(data)
    print("Element counts:", counter)
    print("Most common:", counter.most_common(2))

    print("\n2. defaultdict")
    marks = defaultdict(int)
    marks["Math"] += 85
    marks["Science"] += 90
    print("Marks:", dict(marks))
    print("Non-existing key:", marks["English"]) 

    print("\n3. OrderedDict")
    ordered = OrderedDict()
    ordered["a"] = 1
    ordered["b"] = 2
    ordered["c"] = 3
    print("OrderedDict:", ordered)

    print("\n4. deque")
    dq = deque([1, 2, 3])
    dq.append(4)
    dq.appendleft(0)
    dq.pop()
    dq.popleft()
    print("Deque:", dq)

    print("\n5. ChainMap")
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    combined = ChainMap(dict1, dict2)
    print("ChainMap:", combined)
    print("Value of b:", combined["b"]) 

if __name__ == "__main__":
    collections_demo()
