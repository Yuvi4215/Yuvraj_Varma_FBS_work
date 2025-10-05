### 6. Use a dictionary comprehension to count the length of each word in a sentence (take input from user)
strng = input("Enter the String : ")
# strng = "This is sample string used for coding in the assignment"
di = {key: len(key) for key in strng.split()}
print(f"""Dictionary with key as string and value as length : 
{di}""")