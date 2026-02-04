from functools import reduce

marks = [45, 78, 88, 32, 90, 60]

passed = list(filter(lambda x: x >= 50, marks))
print("Passed Marks:", passed)

grace_marks = list(map(lambda x: x + 5, passed))
print("After Grace Marks:", grace_marks)

total = reduce(lambda a, b: a + b, grace_marks)
print("Total Marks:", total)
