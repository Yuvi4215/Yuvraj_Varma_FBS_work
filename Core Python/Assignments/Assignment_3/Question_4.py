### Write a program to input all sides of a triangle and check whether triangle is valid or not.

# take 3 Side from user as input
base=int(input("Enter Value of Base :: "))
altitude=int(input("Enter Value of Altitude :: "))
hypotenuse=int(input("Enter Value of Hypotenuse :: "))

# perform check
if(hypotenuse== (base**2 + altitude**2)**0.5):
    print(f"For entered Values sides {base, altitude, hypotenuse}, Triangle is valid.")
else:
    print("Triangle is Invalid")

# name="name"
# bol= isinstance(name, str)
# print(f"{bol}")
# print(type(name))