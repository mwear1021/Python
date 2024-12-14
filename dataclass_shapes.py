import math
from dataclasses import dataclass

@dataclass
class Shape:
    pass

@dataclass
class Circle(Shape):
    radius: float

    def get_area(self):
        return f"Area: {math.pi * self.radius ** 2:.2f} cm^2"

    def get_circumference(self):
        return f"Circumference: {2 * math.pi * self.radius:.2f} cm"

@dataclass
class Triangle(Shape):
    side_a : float
    side_b : float

    def hypotenuse(self):
        return math.sqrt(self.side_a ** 2 + self.side_b ** 2)

    def get_area(self):
        side_c = self.hypotenuse()
        p = 0.5 * (self.side_a + self.side_b + side_c)
        total_area = math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - side_c))
        return f"Side C length: {side_c:.2f} cm \nArea: {total_area:.2f} cm^2"

    def get_perimeter(self):
        return f"Perimeter: {self.hypotenuse() + self.side_a + self.side_b:.2f} cm"

@dataclass
class Square(Shape):
    side : float
    def get_area(self):
        return f"Area: {self.side ** 2:.2f} cm^2"

    def get_perimeter(self):
        return f"Perimeter: {self.side * 4:.2f} cm"

# main loop
def shape_loop():
    while True:

        get_shape = input("\n\nEnter 'circle', 'triangle', or 'square' to find area and perimeter (or circumference for circle) or 'exit' to quit: ").strip().lower()

        match get_shape:
            case 'exit':
                print("\nExiting...")
                break

            case "circle":
                get_radius = float(input("\nEnter radius in cm: "))
                shape = Circle(get_radius)
                print(shape.get_area())
                print(shape.get_circumference())

            case "triangle":
                get_side1 = float(input("\nEnter side A length in cm: "))
                get_side2 = float(input("\nEnter side B length in cm: "))
                shape = Triangle(get_side1, get_side2)
                print(shape.get_area())
                print(shape.get_perimeter())

            case "square":
                get_side = float(input("\nEnter a side length in cm: "))
                shape = Square(get_side)
                print(shape.get_area())
                print(shape.get_perimeter())

            case _:
                print("\nNot a valid shape")

if __name__ == "__main__":
    shape_loop()