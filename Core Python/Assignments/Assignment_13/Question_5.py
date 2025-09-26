### 5. Python Program to Sum All the Items in a Dictionary

def getSumFromDict(d):
    dict_sum = 0
    for index in d:
        dict_sum += d[index]
    return dict_sum


d = {"a": 12, "b": 17, "c": 71, "d": 99, "e": 12, "f": 92, "g": 77, "h": 49}
sum = getSumFromDict(d)
print(f"Sum of Dictionary :: {sum}")