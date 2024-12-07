# Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

def calculate(num1, num2):
    CUTOFF = 1000
    product = num1 * num2
    added_total = num1 + num2
    if product <= CUTOFF:
        return product
    else:
        return added_total
        
if __name__ == "__main__":
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    
    print(f"The result is", calculate(n1, n2))