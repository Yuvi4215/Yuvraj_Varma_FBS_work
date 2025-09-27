### map function with lambda
def squere(x):
    return x**2


nums=[1,2,3,4,6,7,8,9]

# result=list(map(lambda x:x**3, nums))
result=list(map( squere, nums))
print(result)