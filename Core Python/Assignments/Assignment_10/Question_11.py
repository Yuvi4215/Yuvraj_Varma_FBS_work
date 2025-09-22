### 11. Write a program to print all numbers which are divisible by m and n in the list.

def getDivisibleList(li, num1, num2):
    new_li = []

    for ele in li:
        if ele % num1 == 0 and ele % num2 == 0:
            new_li += [ele]
    return new_li


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
num1 = int(input("Enter m value : "))
num2 = int(input("Enter n value : "))
print(f"Original list :: {li}")
new_list = getDivisibleList(li, num1, num2)
print(f"Divisible number List : {new_list}")