### reduce 
import functools
nums=[1,2,3,4,5,6,7,8,9,10]

add_ele=functools.reduce(lambda x,y: x+y, nums)
mult_ele=functools.reduce(lambda x,y: x*y, nums)
print(f"Addition       : {add_ele}")
print(f"Multiplication : {mult_ele}")