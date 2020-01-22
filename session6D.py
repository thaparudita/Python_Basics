def square(numbers):
    print(">> [square] numbers is:",numbers, id(numbers))

    for i in range(0, len(numbers)):
        numbers[i] = numbers[i] * numbers[i]


#list in python
numbers = [10, 20, 30, 40, 50]

print(">> numbers is :", numbers, id(numbers))
