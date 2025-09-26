### 9. Python Program to Calculate the Number of Words and the Number of Characters Present in a String


def getNumDigitCount(word):
    word_count, digit_count = 0, 0

    for char in word:
        if char in "0123456789":
            digit_count += 1
            # print(char,end="")
        elif char in "`~!@#$%^&*( )_+-=[]{};':<>,.//?|":
            continue
        else:
            word_count += 1
            # print(char,end="  ")

    return word_count, digit_count


strng = "This is Sample String Used for Coding 1_1!2-2@3=3#4+4$5{5%6}6^7:7&8'8*9(9),./<>?;"

print(f"Original string : {strng}")
str_count, num_count = getNumDigitCount(strng)
print(f"The String Count is :: {str_count}")
print(f"The Digit Count is  :: {num_count}")
