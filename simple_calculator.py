# This code will take 2 numbers (operands) and do math on them with the following operators: +, -, /, *, **

# custom invlaid operator exception class
class InvalidOperatorException(Exception):
    pass

# Create the calculate function and match-case operator with the different symbols
def calculate(num1:float, operator:str, num2:float) -> float:
    '''Calculates a 3-term math expression'''
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '/':
            match num2:
                case 0:
                    raise ZeroDivisionError
            return num1 / num2
        case '*':
            return num1 * num2
        case '**':  # exponent
            return num1 ** num2
        case 'e': # ex: 5 e 2 equals 5 times 10 to the 2nd power => returns 500
            return num1 * (10 ** num2)
        case _: # anything other than the above cases is an invalid operator
            raise InvalidOperatorException(f'Invalid operator: {operator}')

def do_math():
    while True: # repeatedly ask for math expressions from user
        try:
            math_expression = input("Enter a 3-term math expression separated by spaces or type exit to quit: ")

            if math_expression.lower() == 'exit': # exit loop condition
                break
            math_expression = math_expression.split() # split the string into a 3 index list

            if len(math_expression) != 3: # check length of list and raise an error if there aren't 3 list indices
                raise ValueError("Please enter THREE arguments separated by spaces")
            
            # get the 3 arguments from the list indices
            number1 = float(math_expression[0])
            symbol = math_expression[1]
            number2 = float(math_expression[2])

            # send the arguments to the calculate function
            result = calculate(number1,symbol,number2)
            print((f'Result: {result:.2f}'))

        # exceptions 
        except ValueError as ve:
            print(ve)
        except InvalidOperatorException as ioe:
            print(ioe)
        except ZeroDivisionError as zde:
            print(zde)
        except Exception as e:
            print(f'Unexpected Exception: {e}')

if __name__ == "__main__":
    do_math()