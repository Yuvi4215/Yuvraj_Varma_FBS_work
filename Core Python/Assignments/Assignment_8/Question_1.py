### Write a program to calculate area of rectangle


def calculateArea(length, breadh):
    return length * breadh


length = float(input("Enter the length :: "))
breadh = float(input("Enter the breadh :: "))
area = calculateArea(length, breadh)
print(f"Area of Rectangle :: {area}")
