### Test 6- OOP
# 2-20,3-30,4-40,heavy-60


class Vehical:
    
    vehical_basic = {
        "2-Wheeler": 20,
        "3-Wheeler": 30,
        "4-Wheeler": 40,
        "4+_Wheeler": 60,
    }
    allowed = {"2-Wheeler": 2, "3-Wheeler": 3, "4-Wheeler": 4, "4+_Wheeler": 6}
    person_extra = {
        "2-Wheeler": 10,
        "3-Wheeler": 20,
        "4-Wheeler": 40,
        "4+_Wheeler": 100,
    }  # perperson

    def __init__(self, wheels, person):
        print(wheels)
        if wheels in Vehical.vehical_basic:
            self.wheels = wheels
        else:
            self.wheels = "4+_Wheeler"
        self.person = person
        self.extra = self.person - Vehical.allowed.get(self.wheels)
        # print(self.extra)
        if self.extra > 0:
            self.total = Vehical.calculateCharges(self.wheels, self.extra)
        else:
            self.total = Vehical.calculateCharges(self.wheels)

    @staticmethod
    def calculateCharges(veh, ext_per=0):
        # print(Vehical.vehical_basic.get(veh), ext_per)
        return Vehical.vehical_basic.get(veh) + (
            Vehical.person_extra.get(veh) * ext_per
        )

    def __str__(self):
        return f"Vechical : {self.wheels}, Person : {self.person} and Total charges : {self.total}"


v1 = Vehical("2-Wheeler", 3)
v2 = Vehical("3-Wheeler", 4)
v3 = Vehical("4-Wheeler", 5)
v4 = Vehical("5-Wheeler", 6)
v5 = Vehical("6-Wheeler", 7)
v6 = Vehical("7-Wheeler", 8)
print(v1)
print(v2)
print(v3)
print(v4)
print(v5)
print(v6)
