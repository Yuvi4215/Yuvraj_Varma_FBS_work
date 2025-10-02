### 7. Given two sets of numbers, write a Python program to find the missing numbers in the second set
#       as compared to the first and vice versa. Use the Python set.


def missingInSet(set_a, set_b):
    res_a = set()
    res_b = set()

    for elem in set_b:
        if elem not in set_a:
            res_a |= {elem}

    for elem in set_a:
        if elem not in set_b:
            res_b |= {elem}
    return res_a, res_b


a_set = [1, 2, 3, 4, 5]
b_set = [3, 4, 5, 6]
print("Missing in B, Missing in A:", missingInSet(a_set, b_set))