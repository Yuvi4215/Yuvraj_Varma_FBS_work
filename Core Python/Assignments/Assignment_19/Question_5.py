### 5. Find all of the words in a string that are less than 5 letters (take input from user)
strng = input("Enter the String : ")
# strng = "This is sample string used for coding in the assignment"
li = [ele for ele in strng.split() if len(ele) < 5]
print(f"""List of strings that have words with length less than 5 : 
{li}""")