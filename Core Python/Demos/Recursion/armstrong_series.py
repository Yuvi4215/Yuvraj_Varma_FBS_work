###

def getCount(num):
    if num == 0:
        return 0
    return 1 + getCount(num // 10)


def getPower(digit, power):
    if power == 0:
        return 1
    return digit * getPower(digit, power - 1)

def sumOfPower(num, power):
    if num==0:
        return 0
    digit= num%10
    return getPower(digit, power) + sumOfPower(num//10, power)

def isArmstrong(num):
    power=getCount(num)
    if num==sumOfPower(num,power):
        print(f"{num} is- Armstrong number.")
    else:
        print(f"{num} is- NOT Armstrong number.")


num = int(input("Enter the number :: "))
isArmstrong(num)
# print(sumOfPower(num,3))
# print(getCount(num))
# print(getPower(2, 8))
