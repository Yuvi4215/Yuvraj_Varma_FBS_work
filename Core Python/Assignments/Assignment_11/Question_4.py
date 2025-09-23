### 4. Python Program to Find the Second Largest Number in a List Using Bubble Sort


def getSecondMax(li):
    for i in range(0, 3):
        for j in range(i + 1, len(li)):
            if li[i] < li[j]:
                li[j], li[i] = li[i], li[j]
    return li[1]


li = [1.5, 852, 9, 7, 3, 6, 2, 745, 4, 8]

second_max = getSecondMax(li)
print(f"List : ",li)
print("Second MAx Element : ", second_max)
