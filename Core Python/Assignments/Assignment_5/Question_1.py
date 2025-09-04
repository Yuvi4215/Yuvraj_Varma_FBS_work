### Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

user_id = "admin"
password = "admin123"
print("--------------------Start--------------------")
id = input("Enter the User ID :: ")
pswd = input("Enter the password ::")

if user_id == id and password == pswd:
    print("Login succesfull.")
else:
    print("User Id/Password missmatch. you have 3 attempts left.")

    count = 1
    while count < 4:
        print(f"-------------------Attempt number {count}------------")
        id = input("Enter the User ID :: ")
        pswd = input("Enter the password ::")
        count += 1
        if user_id == id and password == pswd:
            print("Login succesfull.")
            break