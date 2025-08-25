### Write a program to check if user has entered correct userid and password.

id='admin'
password='admin007'

#take user input for user id and password
user_id=input("Enter User ID :: ")
pswd=input("Enter Password :: ")

#perform branching
if(user_id== id and pswd==password):
    print("Login Successful")
else:
    print("Invalid userid or password.")