### 1. Create a class Complex Number with data members as real and imag and add following methods :
#       a. Constructor
#       b. Destructor
#       c. Overload +,- operator


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        # print(f"Object : {self.real} + {self.imag}i")

    def __del__(self):
        print(f"!!! Object : {self.real} + {self.imag}i is destroyed !!!")

    def __add__(self, other):
        # print("__add__()")
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        # print("__sub__()")
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


c1 = ComplexNumber(4, 5)
c2 = ComplexNumber(2, 3)

print(f"""
--------------------------------------
Complex Addition : {c1 + c2}
--------------------------------------
      """
      )
print(f"""
--------------------------------------
Complex Subtraction : {c1 - c2}
--------------------------------------      
    """
      )