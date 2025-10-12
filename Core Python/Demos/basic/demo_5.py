# ###
# name=input("enter name : ")
# print(name)
# if name=="main":
#     print("TRUE")

# class Car:
#     def __init__(self, name):
#         self.name=name


# c1= Car("maruti")
# c1.owner="alice"
# print(c1.name, c1.owner)        



class Car:
    total_cars = 0  # static variable

    def __init__(self):
        Car.total_cars += 1

c1=Car()
print(c1.total_cars)
c1.total_cars=20
print(c1.total_cars)
print(Car.total_cars)