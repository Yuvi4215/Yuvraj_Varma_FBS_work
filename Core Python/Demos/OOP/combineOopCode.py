from abc import ABC, abstractmethod

# -------------------------------
# ABSTRACT BASE CLASS
# -------------------------------
class Shape(ABC):
    def __init__(self, color):
        self._color = color  # Protected attribute

    @abstractmethod
    def area(self):
        """Abstract method: must be implemented by subclasses"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method: must be implemented by subclasses"""
        pass

    def show_color(self):
        print(f"The shape color is {self._color}")


# -------------------------------
# INHERITANCE (Single Inheritance)
# -------------------------------
class Rectangle(Shape):
    def __init__(self, width, height, color="blue"):
        super().__init__(color)
        self.__width = width   # Private attribute
        self.__height = height

    # Encapsulation with property getters/setters
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value > 0:
            self.__width = value
        else:
            raise ValueError("Width must be positive")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value > 0:
            self.__height = value
        else:
            raise ValueError("Height must be positive")

    # Implement abstract methods
    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        return f"Rectangle({self.__width}x{self.__height}, color={self._color})"


# -------------------------------
# MULTILEVEL INHERITANCE
# -------------------------------
class Square(Rectangle):
    def __init__(self, side, color="red"):
        super().__init__(side, side, color)

    def __str__(self):
        return f"Square(side={self.width}, color={self._color})"


# -------------------------------
# MULTIPLE INHERITANCE
# -------------------------------
class Printable:
    def print_info(self):
        print(f"Printing object info: {self}")

class ColoredShape(Shape, Printable):
    def __init__(self, color):
        Shape.__init__(self, color)
    
    def area(self):
        return super().area()
    
    def perimeter(self):
        return super().perimeter()


# -------------------------------
# POLYMORPHISM (Method Overriding & Duck Typing)
# -------------------------------
def shape_description(shape):
    """Demonstrates duck typing"""
    print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")
    shape.show_color()


# -------------------------------
# CLASS METHOD & STATIC METHOD
# -------------------------------
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def description(cls):
        return f"This is {cls.__name__}, providing static math utilities."


# -------------------------------
# MAIN PROGRAM
# -------------------------------
if __name__ == "__main__":
    # Create objects
    rect = Rectangle(10, 5, "green")
    sq = Square(7)
    
    print(rect)
    print(f"Area: {rect.area()}, Perimeter: {rect.perimeter()}")
    
    print(sq)
    print(f"Area: {sq.area()}, Perimeter: {sq.perimeter()}")

    # Demonstrate encapsulation
    rect.width = 15
    print(f"Updated Rectangle width: {rect.width}")

    # Demonstrate polymorphism
    for shape in [rect, sq]:
        shape_description(shape)

    # Demonstrate static and class methods
    print(MathUtils.description())
    print(f"Addition using static method: {MathUtils.add(5, 10)}")

    # Demonstrate multiple inheritance
    colored = ColoredShape("yellow")
    colored.print_info()
    colored.show_color()
