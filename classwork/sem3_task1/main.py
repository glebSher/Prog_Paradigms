from classwork.sem3_task1.circle import Circle
from classwork.sem3_task1.triangle import Triangle


def main():
    circle = Circle(5)
    print(f'Площадь круга = {circle.get_area()}')
    print(f'Периметр круга {circle.get_perimeter()}')
    print()

    triangle = Triangle(3, 4, 5)
    print(f'Площадь треугольника = {triangle.get_area()}')
    print(f'Площадь треугольника = {triangle.get_perimeter()}')


if __name__ == '__main__':
    main()
