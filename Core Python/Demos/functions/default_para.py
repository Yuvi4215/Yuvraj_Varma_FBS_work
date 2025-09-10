### Defalut parameter
#1. Assigning value to the parameter in function defination
#2.sequance of mentioning default para is from right to left
#3.invokes optional parameter concept
#4.a-if we pass values to para, then it takes passed value.
#4.b-if we don't value to default para, it will take value from default.

### function type-2st w passing and w/o returning

def add(num1,num2,num3=0, num4=0):
    print("Addition without return para :: ", num1+num2+num3+num4) 

add(10,20,3)

### function type-4st w passing and w returning

def add(num1,num2,num3=0, num4=0):
   return num1+num2+num3+num4 

sum=add(40,10,2)
print("Addition with return para:: ",sum)