### 1. Write a Python program to find elements in a given set that are not in another set.


def differenceSet(set_a, set_b):
    result = set()
    for elem in set_a:
        if elem not in set_b:
            result |= {elem}
    return result


def differenceSet(set_a, set_b):
    result = set_a - set_b
    return result


a = {10, 20, 30, 40, 50, 60}
b = {40, 50, 60, 70, 80, 90}
diff_set = differenceSet(a, b)
print(f"The set A difference B : {diff_set} ")