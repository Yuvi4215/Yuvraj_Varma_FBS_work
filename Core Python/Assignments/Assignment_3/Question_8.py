### Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise failed. (Something like captcha)
import random

id='admin'
password='admin007'
number= random.randint(1000, 9999)

#take user input for user id and password
user_id=input("Enter User ID :: ")
pswd=input("Enter Password :: ")

#perform branching
if(user_id== id and pswd==password):
   print(f"Your Captcha is :: {number}")
   captcha=int(input("Enter Captcha :: "))

   if(captcha==number):
       print("Login Successful")
    
   else:
       print("Wrong Captcha")
else:
    print("Invalid userid or password.")