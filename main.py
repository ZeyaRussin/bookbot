import sys

from stats import get_num_words
from stats import get_character_amount
from stats import get_character_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():

    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    character_amounts = get_character_amount(book_text)
    character_list = get_character_list(character_amounts)

    print(f""" 
============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")

    for entry in character_list:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")

    print("============= END ===============")

main()