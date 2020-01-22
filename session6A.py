print(">>welcome to python app")

num = int(input("enter a number : "))
print(">> 1. num is:", num, id(num))

def square(n):
    global num
    n = n*n
    num = n
    print(">> 2. num is:", n, id(n))
    print(">> 3. num is:", num, id(num))

square(num)
print(">> 4. num is:", num, id(num))