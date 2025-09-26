### 1. Python Program to Add a Key-Value Pair to the Dictionary


def addElementsInDict(key, value):
    d[key] = value


li = ["first", "second", "third", "fourth", "fifth", "sixth"]
d = {}
for i in range(0, len(li)):
    addElementsInDict(i, li[i])
    
print(f"Dictionary :: {d}")