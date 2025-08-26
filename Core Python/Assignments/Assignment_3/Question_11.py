### Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

#Take ages values as input from user
a1=int(input("Enter the age of first person ::"))
a2=int(input("Enter the age of second person ::"))
a3=int(input("Enter the age of third person ::"))
a4=int(input("Enter the age of fourth person ::"))
a5=int(input("Enter the age of fifth person ::"))
cost=float(input("Enter the ticket price ::"))

amount=0

#Perform analysis
# for 1st person
#line of code can be shortend with the use of loop.  
if(a1>59):
    amount=(cost*0.5) + amount
elif(a1<12):
    amount=(cost*0.7) + amount
else:
    amount=cost + amount

# for 2nd person
if(a2>59):
    amount=(cost*0.5) + amount
elif(a2<12):
    amount=(cost*0.7) + amount
else:
    amount=cost + amount

# for 3rd person
if(a3>59):
    amount=(cost*0.5) + amount
elif(a3<12):
    amount=(cost*0.7) + amount
else:
    amount=cost + amount

# for 4th person
if(a4>59):
    amount=(cost*0.5) + amount
elif(a4<12):
    amount=(cost*0.7) + amount
else:
    amount=cost + amount

# for 1th person
if(a5>59):
    amount=(cost*0.5) + amount
elif(a5<12):
    amount=(cost*0.7) + amount
else:
    amount=cost + amount

#display results

print(f"Total amount for {a1,a2,a3,a4,a5} is :: {amount}")