import math
from classwork.sem3_task1.shape import Shape


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_area(self):
        # переменная 'p' - полупериметр треугольника
        p = self.get_perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
