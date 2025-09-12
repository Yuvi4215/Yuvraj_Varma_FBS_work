
def getCount(num):
    if num==0:
        return 0
    return 1+getCount(num//10)

def getPower(digit, power):
    if power==0:
        return 1
    return digit* getPower(digit,power-1)

def sumOfPower(num,power):
    if num==0:
        return 0
    
    digit=num%10
    return getPower(digit,power)+ sumOfPower(num//10, power)


def isArmstrong(num):
    power=getCount(num)

    if num== sumOfPower(num,power):
        print(f"{num}- is Armstrong number.")
    else:
        print(f"{num}- is not Armstrong number.")


# print(getCount(153))
num=int(input("Enter the number ::"))
isArmstrong(num)


# def printPascalpattern(num):

#     for i in range(1, num+1):
#         for j in range(1, num+1-i):
#             print(" ", end= "")
#         val=1
#         for j in range(1,i+1):
#             print(val, end=" ")
#             val= val*(i-j)//(j)
#         print()

# num=5
# printPascalpattern(num)