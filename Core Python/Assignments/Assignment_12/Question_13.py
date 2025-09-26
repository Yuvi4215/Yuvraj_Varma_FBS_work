### 13. Python Program to count number of digits and letters in a string.
def getCharDigitCount(word):
    c_count, d_count = 0, 0

    for ele in word:
        if "0" <= ele <= "9":
            d_count += 1
        elif "a" <= ele <= "z" or "A" <= ele <= "Z":
            c_count += 1
    return c_count,d_count


strng = "A sample String consist chars and digits 12345678900000"
char_count, digit_count = getCharDigitCount(strng)
print(
    f"""
String      : {strng}
----------------------------------------
Char count  : {char_count}
Digit count : {digit_count}
----------------------------------------
"""
)