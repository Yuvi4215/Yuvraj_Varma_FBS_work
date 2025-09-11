def getNumber():
    print("\n\n\n---------------- getNumber ---------------")
    # print("-----------getNumber-----------")
    num = int(input("Enter the number:: "))
    print(f"getNumber-NUM:{id(num)} ---- value::{num}")
    return num


def getCount(num):
    print("\n\n\n---------------- getCount ---------------")
    # print("-----------getCount-----------")
    count = 0
    print(f"getCount-NUM:{id(num)} ---- value::{num}")
    print(f"getCount-count:{id(count)} ---- value::{count}")
    while num > 0:
        num = num // 10
        count += 1
        print(f"getCount(loop)-NUM:{id(num)} ---- value::{num}")
        print(f"getCount(loop)-count:{id(count)} ---- value::{count}")
    return count


def getPower(digit, power):
    print("\n\n\n---------------- getPower ---------------")
    # print("-----------getPower-----------")
    result = 1
    print(f"getPower-DIGIT:{id(digit)} ---- value::{digit}")
    print(f"getPower-POWER:{id(power)} ---- value::{power}")
    print(f"getPower-RESULT:{id(result)} ---- value::{result}")
    
    while power > 0:
        result *= digit
        power -= 1
        print(f"getPower(loop)-POWER:{id(power)} ---- value::{power}")
        print(f"getPower(loop)-RESULT:{id(result)} ---- value::{result}")
    return result


def getSum(num, count):
    print("\n\n\n---------------- getSum ---------------")
    # print("-----------getSum-----------")
    sum = 0
    power = count
    print(f"getSum-NUM:{id(num)} ---- value::{num}")
    print(f"getSum-count:{id(count)} ---- value::{count}")
    print(f"getSum-SUM:{id(sum)} ---- value::{sum}")
    print(f"getSum-POWER:{id(power)} ---- value::{power}")

    while count > 0:
        digit = num % 10
        sum += getPower(digit, power)
        num //= 10
        count -= 1
        print(f"getSum(loop)-DIGIT:{id(digit)} ---- value::{digit}")
        print(f"getSum(loop)-SUM:{id(sum)} ---- value::{sum}")
        print(f"getSum(loop)-NUM:{id(num)} ---- value::{num}")
        print(f"getSum(loop)-count:{id(count)} ---- value::{count}")
    return sum


def isArmstrong(num):
    print("\n\n\n---------------- isArmstrong ---------------")
    # print("-----------isArmstrong-----------")
    print(f"isArmstrong-NUM:{id(num)} ---- value::{num}")
    count = getCount(num)
    sum = getSum(num, count)
    print(f"isArmstrong-count:{id(count)} ---- value::{count}")
    print(f"isArmstrong-SUM:{id(sum)} ---- value::{sum}")
    return sum == num


def startProgramm():
    print("\n\n\n---------------- startProgramm ---------------")
    print("-----------Start-----------")
    print("#153, #370, #371, #407")
    num = getNumber()
    print("\n\n\n---------------- startProgramm ---------------")
    print(f"startProgramm-NUM:{id(num)} ---- value::{num}")
 
    if isArmstrong(num):

        print(f"{num}- is Armstrong Number.")
    else:

        print(f"{num}- 'Not' Armstrong Number.")


startProgramm()
