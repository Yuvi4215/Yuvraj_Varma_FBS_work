### Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

#Take ages values as input from user

cost=float(input("Enter the ticket price ::"))
count=int(input("Enter the count of people ::"))

amount=0
people_list=[]
index=1
while index<=count:
    age=int(input(f"Enter the age for person {index} ::"))
    people_list.append(age)
    index+=1
    if(age>59):
     amount=(cost*0.5) + amount
    elif(age<12):
     amount=(cost*0.7) + amount
    else:
     amount=cost + amount

print(f"Total amount for {people_list} is :: {amount}")