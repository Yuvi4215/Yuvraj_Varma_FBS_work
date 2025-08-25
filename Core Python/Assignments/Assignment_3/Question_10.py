### Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

#Take input for gender and age from user
gender= input('Enter Gender M/F ::')
age=int(input("Enter the age :: "))

#process with if else statement
if(gender=='M' or gender=='male' or gender=='Male'or gender=='m'):
    if(age>=21):
        if(age<40):
            print(f"You are {gender}, your age is {age} and you are Eligible.")
        else:
            print("Visit Kankhal, Haridwar (Uttarakhand) hub of sanyas (renunciation) in India ")

    else:
        print(f"You are {gender} and Your age is {age}. 'NOT ELIGIBLE'")

elif(gender=='F' or gender=='Female' or gender=='female'or gender=='f'):
    if(age>=18):
        if(age<40):
            print(f"You are {gender}, your age is {age} and you are Eligible.")
        else:
            print("Visit Kankhal, Haridwar (Uttarakhand) hub of sanyas (renunciation) in India ")
    else:
        print(f"You are {gender} and Your age is {age}. 'NOT ELIGIBLE'")
else:
    print("you are selected for tester role. ")