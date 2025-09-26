### 7. Python Program to Remove the Given Key from a Dictionary


def removeKeyFromDict(d, key_ele):
    new_dict = {}
    for index in d:
        if key_ele != index:
            new_dict[index] = d[index]
    return new_dict


d={'a': 12, 'b': 17, 'c': 71, 'd': 99, 'e': 12, 'f': 92, 'g': 77, 'h': 49, 'i': 70007, 'j': 1992}
key_ele = input("Enter the key : ")
new_d = removeKeyFromDict(d, key_ele)

print(
    f"""
Original Dictionary           : {d}
Dictionary after removing key : {new_d}
"""
)