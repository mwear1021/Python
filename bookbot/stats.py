def count_words(text):
    words = text.split()
    num_words = len(words)
    return f"Found {num_words} total words"

def character_count(text):
    char_dict = {}
    text = text.lower()
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sorted_dicts(char_dict):
    return sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
