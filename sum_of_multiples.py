# Find the sum of all numbers less than 1000 that are divisible by 3 or 5.

divisible_list = [i for i in range(1,1000) if i % 3 == 0 or i % 5 == 0]
# print(divisible_list)
# print(len(divisible_list))
print(sum(divisible_list))