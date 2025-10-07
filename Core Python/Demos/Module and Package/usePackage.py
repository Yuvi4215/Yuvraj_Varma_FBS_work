### importing package

# # method-1
# from MyPackage import myFunctionFiles
# print(myFunctionFiles.addition(10,20))

# # method-2
# from MyPackage.myFunctionFiles import *
# print(multiplication(10,20))

# # method-3
# from MyPackage.myFunctionFiles import subtraction
# print(subtraction(100, 31))

# method-4
from MyPackage.myFunctionFiles import multiplication as mult
print(mult(10,20))