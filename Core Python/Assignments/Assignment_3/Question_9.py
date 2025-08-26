### Input 5 subject marks from user and display grade(eg.First class,Second class ..)

#Take subject marks as input from user
sub1=int(input("Enter marks for subject one :: "))
sub2=int(input("Enter marks for subject second :: "))
sub3=int(input("Enter marks for subject third :: "))
sub4=int(input("Enter marks for subject fourth :: "))
sub5=int(input("Enter marks for subject fifth :: "))

#perform calculation on subject marks 
if(sub1<100 and sub2<100 and sub3<100 and sub4<100 and sub5<100 and sub1>0 and sub2>0 and sub3>0 and sub4>0 and sub5>0):
    percentage= (sub1+sub2+sub3+sub4+sub5)/500 *100

    if(percentage>75):
        print(f"Grade:-{percentage} - First Class with Distinction.")
    elif(percentage>60):
        print(f"Grade:-{percentage}- First Class.")
    elif(percentage>50):
        print(f"Grade:-{percentage}- Second Class.")
    elif(percentage>35):
        print(f"Grade:-{percentage}- Third Class.")
    else:
        print(f"Grade:-{percentage} Fail.")

else:
    print("Invalid input.")