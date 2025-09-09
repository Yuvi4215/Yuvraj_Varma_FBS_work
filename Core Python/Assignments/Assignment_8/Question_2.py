### Write a program to calculate area of circle


def calculateArea(radius):
    area = 3.1415 * radius * radius
    return area


radius = float(input("Enter the Radius of circle :: "))
area = calculateArea(radius)
print(f"Area of Circle is :: {area}")
