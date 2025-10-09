### Exception 
nu=1/0
try:
    num1=int(input("Enter the Number 1 : "))
    num2=int(input("Enter the Number 2 : "))
    # nu=1/0
except:
    print("!!!! Invalid Input !!!")
else:
    sum=num1+num2
    print(f"Sum of {num1} and {num2} is : {sum}")
finally:
    print("Finally block - END ")