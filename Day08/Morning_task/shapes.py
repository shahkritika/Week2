# A2: Shape abstract class with area() for Circle and Rectangle

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print(f"{self.__class__.__name__} with area = {self.area():.2f}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# --- Test ---
c = Circle(5)
r = Rectangle(4, 6)
c.describe()
r.describe()

