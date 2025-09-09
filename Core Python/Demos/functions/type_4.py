### with passing parameter and with returning value

def checkPerfectNumber(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    return num==sum

num=int(input("Enter the number :: "))
if checkPerfectNumber(num):
    print(f"{num} is- perfect number. ")
else:
    print(f"{num} is- not a perfect number")
