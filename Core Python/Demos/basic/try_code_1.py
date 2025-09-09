
def printPascalpattern(num):

    for i in range(1, num+1):
        for j in range(1, num+1-i):
            print(" ", end= "")
        val=1
        for j in range(1,i+1):
            print(val, end=" ")
            val= val*(i-j)//(j)
        print()

num=5
printPascalpattern(num)