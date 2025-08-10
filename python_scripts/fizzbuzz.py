# Print numbers 1 to 100.
# If divisible by 3, print "Fizz"; if by 5, print "Buzz"; if both, print "FizzBuzz".

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)