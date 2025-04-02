from stats import count_words

def main():
    book_path = "books/frankenstein.txt"
    book_text = read_the_book(book_path)
    print(book_text)
    number_of_words = count_words(book_text)
    print(f"There are {number_of_words} words in this book.")
    number_of_letters = count_letters(book_text)
    print(number_of_letters)
    list = sort_dictionary(book_text)
    print(list)
    construct_report(book_path, book_text)
    

def construct_report(book_path, book_text):
    character_list = sort_dictionary(book_text)
    print(f"--- Begin report of {book_path} ---")
    for character in character_list:
        print(f"The {character[0]} character was found {character[1]} times.")
    print("--- End report ---")

def sort_dictionary(book_text):
    unsorted_dict = count_letters(book_text)
    unsorted_list = list(unsorted_dict.items())
    alpha_unsorted_list = []
    for item in unsorted_list:
        if item[0].isalpha():
            alpha_unsorted_list.append(item)
    alpha_sorted_list = sorted(alpha_unsorted_list)
    return alpha_sorted_list

def count_letters(book_text):
    character_dict = {}
    low_book_text = book_text.lower()
    for character in low_book_text:
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    return character_dict


def  read_the_book(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

main()