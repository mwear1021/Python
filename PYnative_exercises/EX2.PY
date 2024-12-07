# Print the Sum of a Current Number and a Previous number
# Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
current_num = 0
previous_num = 0
for i in range(0,11):
    print(f"current number: {current_num} previous number: {previous_num} sum: {current_num + previous_num}")
    current_num += 1
    previous_num = current_num - 1