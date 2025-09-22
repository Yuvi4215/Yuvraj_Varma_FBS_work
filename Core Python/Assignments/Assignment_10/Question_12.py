### 12. Write a program to create three lists of numbers, their squares and cubes.


def getList(count):
    num, sqr, cub = [], [], []

    for _ in range(0, count):
        ele = int(input("Enter the element : "))
        num += [ele]
        sqr += [ele * ele]
        cub += [ele * ele * ele]
    return num, sqr, cub


count = int(input("Enter the number of elements to add in list :"))
number, squre, cube = getList(count)
print(f"Number List : {number}")
print(f"Squre List  : {squre}")
print(f"Cube List   : {cube}")