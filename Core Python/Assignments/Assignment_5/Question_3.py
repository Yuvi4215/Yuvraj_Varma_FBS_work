### Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

print("--------------------Start--------------------")
passengers = int(input("Enter Total number of passengers :: "))
cost = int(input("Enter ticket cost :: "))
amount = 0.0
index = 1
print("--------------------Ages--------------------")
while passengers > 0:
    age = int(input(f"Enter Age for number {index} passanger :: "))
    index += 1
    passengers -= 1
    if age < 12:
        amount += cost * 0.7
    elif age > 59:
        amount += cost * 0.5
    else:
        amount += cost
print("--------------------Result--------------------")
print(f"Total fare :: {amount}")