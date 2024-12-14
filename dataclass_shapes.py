"""
Shape Calculator Script
This program allows the user to calculate the area and perimeter (or circumference)
of various geometric shapes like circles, triangles, and squares.
"""


import math
from dataclasses import dataclass

@dataclass
class Shape:
    """Base class for all shapes."""
    pass

@dataclass
class Circle(Shape):
    """
    Represents a circle with a radius.

    Methods:
    area: Calculates the area of the circle.
    circumference: Calculates the circumference of the circle.
    """
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
        """
        Calculates the hypotenuse (side_c) of the triangle
        using the Pythagorean theorem.
        Returns:
            float: The length of the hypotenuse.
        """
        return math.sqrt(self.side_a ** 2 + self.side_b ** 2)

    def get_area(self):
        """
        Calculates the area of the triangle using Heron's formula.
        Returns:
            str: The area of the triangle as a formatted string.
        """
        side_c = self.hypotenuse()
        p = 0.5 * (self.side_a + self.side_b + side_c)  # Semi-perimeter of the triangle.
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

def shape_loop():
    """
    Interactive loop for calculating properties of different shapes.
    Prompts the user for the shape type and dimensions, then displays results.
    """
    while True:
        # Prompt the user for the shape type or to exit the program.
        get_shape = input("\n\nEnter 'circle', 'triangle', or 'square' to find area and perimeter (or circumference for circle) or 'exit' to quit: ").strip().lower()

        # Handle each shape type or exit the loop.
        match get_shape:
            case 'exit':
                print("\nExiting...")
                break

            case "circle":
                # Get radius input and create Circle instance
                get_radius = float(input("\nEnter radius in cm: "))
                shape = Circle(get_radius)
                print(shape.get_area())
                print(shape.get_circumference())

            case "triangle":
                # Get side lengths and create Triangle instance
                get_side1 = float(input("\nEnter side A length in cm: "))
                get_side2 = float(input("\nEnter side B length in cm: "))
                shape = Triangle(get_side1, get_side2)
                print(shape.get_area())
                print(shape.get_perimeter())

            case "square":
                # Get side length and create Square instance
                get_side = float(input("\nEnter a side length in cm: "))
                shape = Square(get_side)
                print(shape.get_area())
                print(shape.get_perimeter())

            case _:
                # Invalid input case
                print("\nNot a valid shape")

if __name__ == "__main__":
    shape_loop()