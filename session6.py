def show(num):
    print(num)
    num -= 1
    if num == 0:
        show(num)
        return


show(10)