### 3. Count the number of spaces in a string (take input from user)/
strng=input("Enter the String : ")
# strng = "fg ghj lkj hjkl jhfgi kjhgtyu i      kjh"
space_sum = sum(1 for ele in strng if ele == " ")
print(f"String containt total : {space_sum} spaces")