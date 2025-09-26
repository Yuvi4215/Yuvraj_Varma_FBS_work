### 10. Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions

def getLongerString(word1,word2):
    w1,w2=0,0
    for _ in word1:
        w1+=1
    for _ in word2:
        w2+=1
    
    if w1==w2:
        return "Both Strings are of same length"
    elif w1>w2:
        return word1
    else:
        return word2



str1=input("Enter the first String  :: ")
str2=input("Enter the second String :: ")

final_str=getLongerString(str1,str2)
print(f"Output :: {final_str}")