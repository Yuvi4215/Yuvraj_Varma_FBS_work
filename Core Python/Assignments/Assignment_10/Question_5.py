### Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.


def getPresentCount(li, value):
    count = 0
    for ele in li:
        if value == ele:
            count += 1

    return count


li = [2, 78, 88, 12, 2, 88, 9, 2, 78, 2, 1, 33, 69]

value = int(input("Enter the element :: "))
count = getPresentCount(li, value)
if count != 0:
    print(f"Element-{value} Present, {count} times. ")
else:
    print(f"Element-{value} Not Found.")
