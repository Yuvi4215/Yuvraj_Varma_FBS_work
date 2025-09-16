###car class
class Car:
    ### default constructor
    def __init__(self,brand="defalut", model="default", volume=0.0, price=0.0, availablity=False):
        self.brand=brand
        self.model=model
        self.volume=volume
        self.price=price
        self.availablity=availablity

    # ### parameterized constructor
    # def __init__(self,brand, model, volume, price, availablity):
    #     self.brand=brand
    #     self.model=model
    #     self.volume=volume
    #     self.price=price
    #     self.availablity=availablity


    # def setData(self, brand, model, volume, price, availablity):
    #     self.brand=brand
    #     self.model=model
    #     self.volume=volume
    #     self.price=price
    #     self.availablity=availablity

    def getData(self):
        data=f" Brand:: {self.brand}\n Volume:: {self.volume}\n Price:: {self.price}\n Availability:: {self.availablity}"
        return data
        
    def start(self):
        print("Car is stared.")

    def stop(self):
        print("Car is stopped.")

# c1=Car("BMW", "V3" ,27.9, 7899999,False)
c2=Car()
print(c2.getData())
c2.start()
c2.stop()

# c1.setData("BMW", "V3" ,27.9, 7899999,False)
# data=c1.getData()
# print(data)
# c1.start()
# c1.stop()