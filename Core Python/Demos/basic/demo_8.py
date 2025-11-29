def is_prime(num):
    if num<2:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    else:
        return True
    
if __name__=="__main__":
    # if is_prime(2):
    #     print("prime")
    # else:
    #     print("not prime")

    # for num in range(2, 101):
    #     if is_prime(num):
    #         print(num, end=" ")

    count=0
    num=2
    while count<7:
        if is_prime(num):
            print(num, end=" ")
            count+=1
        num+=1
