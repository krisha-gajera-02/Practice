# functools Library

from functools import  reduce, partial, cmp_to_key, total_ordering

print("\n1. reduce:")
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)

print("\n2. partial:")

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print("Square of 5:", square(5))
print("Cube of 3:", cube(3))

print("\n3. cmp_to_key:")

def compare(a, b):
    return a - b  

data = [5, 2, 9, 1, 7]
sorted_data = sorted(data, key=cmp_to_key(compare))
print("Sorted Data:", sorted_data)

print("\n4. total_ordering:")

@total_ordering
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

    def __lt__(self, other):
        return self.marks < other.marks

    def __repr__(self):
        return f"{self.name} ({self.marks})"

students = [
    Student("Aman", 85),
    Student("Krisha", 92),
    Student("Mayur", 88)
]

print("Students sorted by marks:")
print(sorted(students))
