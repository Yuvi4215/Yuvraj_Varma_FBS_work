### Write a program to check if given number is Armstrong or not using recursive function.

def getCount(num):
    if num==0:
        return 0
    return 1+ getCount(num//10)

def getPower(digit,count):
    if count==1:
        return digit
    return digit* getPower(digit,count-1)

def getSum(num,count):
    if num==0:
        return 0
    digit=num%10
    return getPower(digit, count)+ getSum(num//10,count)

def isArmstrong(num):
    count= getCount(num)

    if getSum(num,count)==num:
        print(f"{num} is- 'Armstrong number.'")
    else:
        print(f"{num} is- 'NOT Armstrong Number'")


num=int(input("Enter the number :: "))
isArmstrong(num)