students = {"John", "Jennie", "Jim", "Jack", "Joe"}
print(students, id(students))
print(type(students))

newstudents = (students + {"Fionna", "George"})
print(newstudents, id(newstudents))

print(students, id(students))
print(newstudents, id(newstudents))

students = (students + {"Fionna", "George"})
print(students, id(students))

print()
