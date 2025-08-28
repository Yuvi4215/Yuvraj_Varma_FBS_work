# user input
num=int(input("Enter Iteration number :: "))
#while loop 
while(num>0):
    print(f"Direct number decrement- {num}")
    num-=1

num=int(input("Enter Iteration number :: "))
#while loop using another variable
i=0
while(i<num):
    i+=1
    print(f"Another variable increment- {i}") 