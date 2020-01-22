data = [1, 2, 3, 4, 5]
print(len(data))
print(max(data))
print(min(data))


def mylen(data):
    length = 0
    return length

def mymax(data):
    max = 0
    return mymax

def mymin(data):
    min = 0
    return mymin


# List Comprehension

print([x**2 for x in data])


productprices = [1241, 2654, 1793, 7954, 4615]
#list comprehensions and expressions : ERROR

print([x = x - 0.4*x, for x in productprices])

numbers = list(range(1, 101))
print(numbers)

names1 = ("John", "Jennie", "Jim", "John", "Jack")
names2 = list(names1)
names3 = set(names1)
# names4 = dict(names1) | Error

print(names1, type(names1))
print(names2, type(names2))
print(names3, type(names3))

