# Write a Python code to remove characters from a string from 0 to n and return a new string.
def remove_n_chars(user_string, n_chars):
    try:
        user_string = list(user_string)
        if n_chars > len(str(user_string)):
            raise ValueError("n can't be greater than thew string length")
        return user_string[n_chars:]
    except ValueError as ve:
        print(ve)
        return None

def get_string():
    original_string = input("Enter a string: ")
    n = int(input("Enter first n-number of characters to remove from the front of the string: "))

    new_string = remove_n_chars(original_string, n)
    if new_string is not None:
        print(f"New string:", ''.join(new_string))

if __name__ == "__main__":
    get_string()