# Given a list with duplicates, return a list with only unique elements

list_with_duplicates = [1, 2, 3, 1, 2, 3, 5, 6, 7, 8, 8, 7]

# cast as a set to remove duplicates
normalized_list = set(list_with_duplicates)

# cast the set back to a list
print(list(normalized_list))

# count unique occurences
print(len(list(normalized_list)))

