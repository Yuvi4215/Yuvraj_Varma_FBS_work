### 3. Python Program to Check if a Given Key Exists in a Dictionary or Not

def isKeyPresent(di, key):
    for key_ele in di:
        if key_ele == key:
            return True
    return False


di={'a': 12, 'b': 17, 'c': 71, 'd': 99, 'e': 12, 'f': 92, 'g': 77, 'h': 49, 'i': 70007, 'j': 1992}
key = input("Enter the key element : ")

if isKeyPresent(di, key):
    print(f"KEY :{key}- is present.")
else:
    print(f"KEY :{key}- Not Found!")