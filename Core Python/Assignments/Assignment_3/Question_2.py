### Write a program to input any alphabet and check whether it is vowel or consonant.

# take character input from user
alphabet=input("Enter the single alphabet :: ")
count=len(alphabet)

#    use branching 
if(count==1):
    if(alphabet in 'aeiouAEIOU'):
        print(f"{alphabet} is vowel.")
    else:
        print(f"{alphabet} is consonant.")
else:
    print("Wrong input")