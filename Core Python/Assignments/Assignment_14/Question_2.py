### 2. Write a Python program to remove the intersection of a second set with a first set.


def interstionSet(set_a, set_b):
    result = set()

    if len(set_a) > len(set_b):
        for ele in set_a:
            if ele in set_b:
                result |= {ele}
    else:
        for ele in set_b:
            if ele in set_a:
                result |= {ele}
    return result


a = {10, 20, 30, 40}
b = {30, 40, 50, 60, 70, 80, 90, 10}
intersection_set = interstionSet(a, b)
print(f"Intersection of A and B set : {intersection_set}")