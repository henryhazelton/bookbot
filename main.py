from stats import count_words
from stats import count_letters
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = read_the_book(book_path)
    number_of_words = count_words(book_text)
    print(f"{number_of_words} words found in the document")
    number_of_letters = count_letters(book_text)

    list = sort_dictionary(book_text)
    construct_report(book_path, book_text)
    

def construct_report(book_path, book_text):
    character_list = sort_dictionary(book_text)
    print(f"--- Begin report of {book_path} ---")
    for character in character_list:
        print(f"{character[0]}: {character[1]}")
    print("--- End report ---")

def sort_dictionary(book_text):
    unsorted_dict = count_letters(book_text)
    unsorted_list = list(unsorted_dict.items())
    alpha_unsorted_list = []
    for item in unsorted_list:
        if item[0].isalpha():
            alpha_unsorted_list.append(item)
    alpha_sorted_list = sorted(alpha_unsorted_list, key=lambda x: x[1], reverse=True)
    return alpha_sorted_list




def  read_the_book(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

main()