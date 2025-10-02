### 9. Write a Python program to find all the unique combinations of 3 numbers from a given list
#      of numbers, adding up to a target number.


def combinationTriplets(nums, target):
    unique = []
    for n in nums:
        if n not in unique:
            unique.append(n)

    combination = []
    n = len(unique)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if unique[i] + unique[j] + unique[k] == target:
                    triplet = tuple(sorted([unique[i], unique[j], unique[k]]))
                    if triplet not in combination:
                        combination.append(triplet)
    return combination


nums = [3, 1, 2, -1, -2, 0]
target = 2
print("Triplets:", combinationTriplets(nums, target))