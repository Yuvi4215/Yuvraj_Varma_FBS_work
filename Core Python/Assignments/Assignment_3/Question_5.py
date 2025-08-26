### Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

#Take side values from user as input
s1=int(input("Enter Value of Base :: "))
s2=int(input("Enter Value one side :: "))
s3=int(input("Enter Value another side :: "))

# perform branching 
if s1 > 0 and s2 > 0 and s3 > 0 and (s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1):
    if(s1 == s2 == s3):
        print(f"For given input ({s1}, {s2}, {s3}) → Triangle is Equilateral.")
    elif(s1 == s2 or s2 == s3 or s1 == s3):
        print(f"For given input ({s1}, {s2}, {s3}) → Triangle is Isosceles.")
    else:
        print(f"For given input ({s1}, {s2}, {s3}) → Triangle is Scalene.")
else:
    print("The given side lengths do not form a valid triangle.")