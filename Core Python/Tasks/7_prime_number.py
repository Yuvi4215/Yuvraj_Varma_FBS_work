#num=int(input("enter number :: "))
num= 85

for index in range(2,num):
    if num%index ==0:
        print(f"number {num} is not a Prime Number")
        break
else:
    print(f"number {num} is Prime Number.")
      
