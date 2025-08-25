### Write a program to input angles of a triangle and check whether triangle is valid or not.

# take 3 angles from user as input
angle1=int(input("Enter first angle :: "))
angle2=int(input("Enter Second angle :: "))
angle3=int(input("Enter Third angle :: "))
if(angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1+angle2+angle3)==180):
    print(f"For entered angle values of {angle1, angle2, angle3}, Triangle is valid.")
else:
    print("Triangle is not valid. ")