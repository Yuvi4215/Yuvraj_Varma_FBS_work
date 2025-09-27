### check prime using Lambda

def isPrime(number):
    if number<2:
        return False
    else:
        for ele in range(2, int(number**0.5)+1):
            if number% ele==0:
              return False
        else:
              return True


nums=[0,1,2,3,4,5,6,7,8,9,10]
result= list(map(isPrime, nums))
print(result)


