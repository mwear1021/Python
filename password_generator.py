# Create a script to generate secure random passwords.

import string
import random

length_of_password = int(input("Enter the length of the random password: "))    # get length of password

possible_chars = '' # create empty string
possible_chars += string.ascii_letters  # add letters and capital letters
possible_chars += string.digits # add numbers
possible_chars+= string.punctuation # add symbols

new_password = ''
for i in range(0, length_of_password):
    new_password += random.choice(possible_chars)   # add a random character from possible_chars to new_password str

print("Random password:", new_password)