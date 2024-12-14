# 1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
# from math import pi
#
# class Circle:
#     def __init__(self, radius:float) -> None:
#         self.radius = radius
#
#     def find_area(self):
#         return f"Area: {pi * (self.radius ** 2):.2f}"
#
#     def find_circumference(self):
#         return f"Circumference: {pi * (self.radius * 2):.2f}"
#
# circle1 = Circle(4.5)
#
# print(circle1.find_area())
# print(circle1.find_circumference())




#2. Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
"""from datetime import datetime
from datetime import date

from dateutil.utils import today


class Person:
    def __init__(self, name, country, birth_year):
        self.name = name
        self.country = country
        self.birth_year = birth_year


    def find_age(self):
        current_year = datetime.now().year
        birthdate_year = self.birth_year
        age = current_year - birthdate_year
        return f"Age of {self.name}: {age}"

person1 = Person("Arnold", "Austria", 2004)

print(person1.find_age())"""






#  Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return f"Sum: {self.num1 + self.num2}"

    def subtract(self):
        return f"Difference: {self.num1 - self.num2}"

    def multiply(self):
        return f"Product: {self.num1 * self.num2}"

    def divide(self):
        if self.num2 != 0:
            return f"Quotient: {self.num1 + self.num2}"
        else:
            return "Cannot divide by zero"

    def exponent(self):
        return f"{self.num1} to the {self.num2} = {self.num1 ** self.num2}"

number1 = float(input("Enter the first number: "))
operator = input("Enter math operator: ")
number2 = float(input("Enter the second number: "))

operation = Calculator(number1, number2)

match operator:
    case "+":
        print(operation.add())
    case "-":
        print(operation.subtract())
    case "*":
        print(operation.multiply())
    case "/":
        print(operation.divide())
    case "**":
        print(operation.exponent())
    case _:
        print("Invalid operator")


