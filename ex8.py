class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student Name: {self.name}, Marks: {self.marks}"

    def __add__(self, other):
        return self.marks + other.marks

    def __len__(self):
        return len(self.name)

    def __eq__(self, other):
        return self.marks == other.marks

s1 = Student("Krisha", 85)
s2 = Student("Aditi", 85)

print(s1)                 
print("Total Marks:", s1 + s2)   
print("Name Length:", len(s1))   
print("Same Marks?", s1 == s2)   
