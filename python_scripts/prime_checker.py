# Write a function to check if a number is prime
from sympy import *

def is_prime(num):
    return isprime(num)

prime_list = []

for i in range(1, 10001):
    if is_prime(i):
        prime_list.append(i)

print(len(prime_list))

