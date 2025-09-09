def getNumber():
    # print("-----------getNumber-----------")
    num = int(input("Enter the number:: "))
    return num


def getCount(num):
    # print("-----------getCount-----------")
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count


def getPower(digit, power):
    # print("-----------getPower-----------")
    result = 1
    while power > 0:
        result *= digit
        power -= 1
    return result


def getSum(num, count):
    # print("-----------getSum-----------")
    sum = 0
    power = count
    while count > 0:
        digit = num % 10
        sum += getPower(digit, power)
        num //= 10
        count -= 1
    return sum


def isArmstrong(num):
    # print("-----------isArmstrong-----------")
    count = getCount(num)
    sum = getSum(num, count)
    return sum == num


def startProgramm():
    print("-----------Start-----------")
    print("#153, #370, #371, #407")
    num = getNumber()

    if isArmstrong(num):
        print(f"{num}- is Armstrong Number.")
    else:
        print(f"{num}- 'Not' Armstrong Number.")


startProgramm()
