#  Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return f"{self.num1} + {self.num2} = {self.num1 + self.num2}"

    def subtract(self):
        return f"{self.num1} - {self.num2} = {self.num1 - self.num2}"

    def multiply(self):
        return f"{self.num1} * {self.num2} = {self.num1 * self.num2}"

    def divide(self):
        if self.num2 != 0:
            return f"{self.num1} / {self.num2} = {self.num1 + self.num2}"
        else:
            return "Cannot divide by zero"

    def exponent(self):
        return f"{self.num1} ^ {self.num2} = {self.num1 ** self.num2}"

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
