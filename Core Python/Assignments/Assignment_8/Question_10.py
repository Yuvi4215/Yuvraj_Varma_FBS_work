### Write a program to check if entered year is a leap year or not.


def isLeapYear(year):
    if year % 4 == 0 and (year != 100 or year % 400 == 0):
        return True
    else:
        return False


year = int(input("Enter the year: "))
if isLeapYear(year):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is NOT a Leap Year.")
