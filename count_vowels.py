# Write a function that takes a string and returns the number of vowels

def count_the_vowels(user_string):
    num_of_vowels = []
    VOWELS = "aeiou"
    for letter in user_string.lower():
        if letter in VOWELS:
            num_of_vowels.append(letter)
    return len(num_of_vowels)

get_string = str(input("Enter a string and I'll count the vowels\n> "))
num_of_vowels = count_the_vowels(get_string)
print(f"The string you entered contains {num_of_vowels} vowels")