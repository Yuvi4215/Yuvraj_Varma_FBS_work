### Bubble Sort


def bubbleSort(li):
    for i in range(1, len(li)):
        for j in range(0, len(li) - i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    return li


li = [60, 50, 40, 30, 20, 10]
print(li)
li1 = bubbleSort(li)
print(f"List after Bubble sort :: {li1}")


def selectionSort(li):
    for i in range(0, len(li) - 1):
        index = i
        for j in range(i + 1, len(li)):
            if li[index] > li[j]:
                index = j
        li[index], li[i] = li[i], li[index]
    return li


li = [60, 50, 40, 30, 20, 10]
li1 = selectionSort(li)
print(f"List after Selection sort :: {li1}")
