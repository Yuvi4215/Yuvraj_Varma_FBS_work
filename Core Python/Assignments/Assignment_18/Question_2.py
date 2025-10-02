### 2. Create a class Distance with data members as km,m and cm and add following methods :
#       a. Constructor
#       b. Destructor
#       c. Overload +,- operator


class Distance:
    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm
        print(f"Distance object created : {self.km}km {self.m}m {self.cm}cm")

    def __del__(self):
        print(f"Distance object : {self.km}km {self.m}m {self.cm}cm is destroyed")

    def __normalize(self):
        print("Private method called.")
        self.m += self.cm // 100
        self.cm = self.cm % 100

        self.km += self.m // 1000
        self.m = self.m % 1000

    def __add__(self, other):
        result = Distance(self.km + other.km, self.m + other.m, self.cm + other.cm)
        result.__normalize()
        return result

    def __sub__(self, other):
        total_self = self.km * 100000 + self.m * 100 + self.cm
        total_other = other.km * 100000 + other.m * 100 + other.cm

        if total_self < total_other:
            return "Error : negative distance"

        diff = total_self - total_other
        km = diff // 100000
        diff = diff % 100000

        m = diff // 100
        cm = diff % 100

        return Distance(km, m, cm)

    def __str__(self):
        return f"{self.km} km, {self.m} m, {self.cm} cm"


d1 = Distance(2, 700, 78)
d2 = Distance(12, 981, 99)

print(
    f"""
-------------------------------------------------
Distance Addition : {d1 + d2}
-------------------------------------------------
"""
)
print(
    f"""
-------------------------------------------------
Distance Subtraction : {d1 - d2}
-------------------------------------------------
"""
)