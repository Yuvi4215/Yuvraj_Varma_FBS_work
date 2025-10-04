###

def pascalTriangle(n):
    prev = []

    for row in range(n):
        curr = [1] * (row + 1)
        for col in range(1, row):
            curr[col] = prev[col - 1] + prev[col]
        prev = curr
        print(str(curr).strip("[]"))
        

pascalTriangle(6)