# something like pass  by value but there is only pass by reference  | as value


def square(num):
    num = num * num
    print(">> [square] num  is :", num, id(num))


num = 10
print(">> [main] num is:", num, id(num))
square(num)
print(">> [main] num now is:", num, id(num))
