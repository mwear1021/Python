# Count the frequency of each word in a string. Ignore case and punctuation
user_string = str(input("Enter a string to have the words and occurences of those words shown\n> ")).lower().split()

dict_of_words = {}

for item in user_string:
    if item in dict_of_words:
        dict_of_words[item] += 1
    else:
        dict_of_words[item] = 1

for k,v in dict_of_words.items():
    print(f"{k}: {v}")

