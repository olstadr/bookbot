import sys

def get_book_text(path):
    with open(path) as b:
    # do something with b (the book) here
        # b is a book
        book_text = b.read()
        return book_text

from stats import get_num_words
from stats import get_character_count
from stats import get_list_of_dict
from stats import sort_on

def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(path)
    word_counter = get_num_words(book_text)
    characters_dict = get_character_count(book_text)
    sorted_dict = get_list_of_dict(characters_dict)
    sorted_dict.sort(reverse=True, key=sort_on)
    report_header = f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {word_counter} total words
--------- Character Count -------
"""
    report_closing = "============= END ==============="
    print(report_header)
    for character in sorted_dict:
        if character["char"].isalpha():
            print(f"{character['char']}: {character['num']}")
    print(report_closing)
    return

main()
    # calling main for future use
