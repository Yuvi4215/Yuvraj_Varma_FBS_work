print("-----------------1st pass--> to neglect indentation started error.----------------------")
#1st pass--> to neglect indentation started error.
for i in range(1,20):
    pass
print("----------------2nd Break--> to terminate the loop forfully-----------------------")
#2nd Break--> to terminate the loop forfully
for i in range(1,6):
    if i==3:
        break
    print(i)
print("------------------#3rd Continue--> to Skip current iteration and loop continue with next iteration---------------------")
#3rd Continue--> to Skip current iteration and loop continue with next iteration
for i in range(1,6):
    if i==3:
        continue #if lines of code are present after continue it will not exicute 
    print(i)
print("-------------------4th else--> this block will exicute after succesfull exicution of loop--------------------")
#4th else--> this block will exicute after succesfull exicution of loop
for i in range(1,6):
    print(i)
else:
    print("The ELSE block exicuted")