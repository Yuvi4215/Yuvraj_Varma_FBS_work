### Write a program to input all sides of a triangle and check whether triangle is valid or not.

# take 3 Side from user as input
s1 = int(input("Enter first side: "))
s2 = int(input("Enter second side: "))
s3= int(input("Enter third side: "))

if s1 > 0 and s2 > 0 and s3 > 0 and (s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1):
    print(f"For entered side values {s1}, {s2}, {s3} → Triangle is valid.")
else:
    print("Triangle is not valid.")
# name="name"
# bol= isinstance(name, str)
# print(f"{bol}")
# print(type(name))