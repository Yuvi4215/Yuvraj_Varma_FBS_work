### 7. Write a program to create a new list from existing list which contains cube of each number of list.


def getCubeList(li, power=3):
    new_list = []
    for ele in li:
        val = ele
        for _ in range(0, power - 1):
            val *= ele
        new_list += [val]

    return new_list


li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
power = int(input("Enter the power : "))

print(f"Original list :: {li}")
# print(f"New List :: {getCubeList(li)}")
print(f"New List :: {getCubeList(li,power)}")
