def add(plus):
    plus = num1 + num2
    print(">> num1 + num2 = ", plus )


def sub(minus):
    minus = num1 - num2
    print(">> num1 + num2 = ", minus)


def multiply(product):
    product = num1 * num2
    print(">> num1 + num2 = ", product)


def divide(div):
    if num1 > num2 :
        div = num1 / num2
        print(">> num1 / num2 = ", div)
    else:
        div = num2 / num1
        print(">> num2 / num1 = ",div)


num1 = float(input(">> ENTER NUMBER 1 :", num1))
num2 = float(input(">> ENTER NUMBER 2 :", num2))

add()
sub()
multiply()
divide()








