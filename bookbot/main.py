# This is the main entry point for the BookBot application. It reads a book from a specified file path, analyzes its content, and prints out statistics - word count and character count.

from stats import count_words, character_count, sorted_dicts
import sys

def get_book_text(path_to_file):
    with open(path_to_file, 'r') as f:
        return f.read()
    
def main():
    if len(sys.argv) == 2:
        filepath = sys.argv[1]
        book_text = get_book_text(filepath)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(count_words(book_text))
        print("------- Character Count --------")
        for char, count in sorted_dicts(character_count(book_text)):
            print(f"{char}: {count}")
        print("============= END ===============")
    else: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()