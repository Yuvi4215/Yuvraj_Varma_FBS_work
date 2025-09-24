### 8. Print 1 to 100 in snakes and ladder pattern.


def printSnakePattern(num):
    for i in range(num, 0, -1):
        if i % 2 == 0:
            step = i * 10
            for j in range(step, step - 10, -1):
                if j > 99:
                    print(j, end="   ")
                else:
                    print(j, end="    ")
        else:
            step = (i - 1) * 10
            for j in range(step+1, step + 11):
                if j < 10:
                    print(j, end="     ")
                else:
                    print(j, end="    ")
        print()


rows = 10
printSnakePattern(rows)