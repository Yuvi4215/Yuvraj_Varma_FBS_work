### Write a program to reverse a given number using recursive function.

# method-1, coverting into string
def getReverseStr(num):
    if num<10:
        return str(num)

    return str(num%10)+ getReverseStr(num//10)



# not working if zero at end
def getMultiplier(num):
    if num==0:
        return 1
    return 10*getMultiplier(num//10)

def getReverse(num):
    if num < 10:
        return num
    digit = num % 10
    return (digit * getMultiplier(num))//10 + getReverse(num // 10)

#num=6900
num=int(input("Enter the number :: "))
print("------------Using String type converion and output as string--------------")
print(f"original:{num} Reverse digit ::", getReverseStr(num))
print("\n------------Using String type converion and output as int--------------")
print(f"original:{num} Reverse digit ::", int(getReverseStr(num)))
print("\n------------Method 2--------------")

print("method-2 :: ", getReverse(num))