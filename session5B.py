# iterations and loops
num = int(input("enter a num:"))
i = 1

while i<= 10:
    print(num, "", i, "is equal to", (num*i))
    i+=1

print(">>>><<<<")

for i in range(10, 0, -1):
    print(num, "", i, "is equal to", (num*i))
