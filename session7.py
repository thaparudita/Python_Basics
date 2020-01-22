"""
sequences in python
sequence : data with quite similar type

sequences listed below is also known as built in DS here in python

Why data is to be Structured ?
1. Sort
2. Search
3. Filter
PS :
"""

students = ("John", "Jennie", "Jim", "Jack", "Joe")
print(students)
print(type(students))
# CONCATENATION | IMMUTABLE
newstudents = (students + ("Fionna", "George"))
print(newstudents)

print(students)
print()

# REPETITION

print(students*2)                   # new tuple

# MEMBERSHIP TESTING

print("John" in students)
print("Dave" not in students)


# INDEXING

print(students[0])
print(students[len(students-1)])

# SLICING

print(students[0:2])                # picking items from a range where 0 is inclusive and 2 is not
filteredstudents = students[1:4]
print(filteredstudents)

print()

# basic for loop
# for i in range(0, len(students)):
# print(student[i])


# Enhanced version for loop | for-each loop

for student in students:
    print[student]

