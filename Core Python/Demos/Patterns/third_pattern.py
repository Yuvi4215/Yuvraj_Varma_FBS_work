num = 7
### 1. Increment Pattern
for i in range(1, num + 1):  # 1 → 7
    for j in range(i):
        print("*", end=" ")
    print()

print("-----------------Next pattern----------------")
### 2. Decrement Pattern
for i in range(1, num + 1):  # 1 → 7
    for j in range(num - i + 1):  # decreasing stars
        print("*", end=" ")
    print()

print("-----------------Next pattern----------------")
for i in range(1, 2*num):  # 1 → 13
    if i <= num:
        for j in range(i):  # Increasing part
            print("*", end=" ")
    
    else:
        for j in range(2*num - i):     # Decreasing part
            print("*", end=" ")
    print()   