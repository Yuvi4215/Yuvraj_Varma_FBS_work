# input number from user

num= int(input('Enter the Number :: '))

if(num>=0):
    if(num>50):
        if(num>100):
            print(f"number {num} is greater than 100")

        else:
         print(f"number {num} is greater than 50")

    else:
        print(f"number {num} is between 0 to 50 category.")

else:
    print(f"Number {num} is less than zero.")