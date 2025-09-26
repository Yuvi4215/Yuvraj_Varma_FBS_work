### 6. Python Program to Multiply All the Items in a Dictionary


def getDictItemMulti(d1):
    multi_dict = 1
    for index in d1:
        multi_dict *= d1[index]
    return multi_dict


d1 = {"a": 12, "b": 1, "c": 7, "d": 9, "e": 2, "f": 6}
multiply = getDictItemMulti(d1)
print(f"Multiplication of Dictionary Items :: {multiply}")