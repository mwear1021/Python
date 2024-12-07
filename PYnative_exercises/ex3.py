# Write a Python code to accept a string from the user and display characters present at an even index number.

s = input("Enter a string: ")
print("Original string: ", s)
empty_list = []

for i in s[0::2]:
    empty_list.append(i)

even_index_chars = " ".join(empty_list)
print("Every other character:", even_index_chars)