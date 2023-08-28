def main():
    book_path = "books/frankenstein.txt"
    book_text = read_the_book(book_path)
    print(book_text)
    number_of_words = count_words(book_text)
    print(f"there are {number_of_words} words in this book.")
    number_of_letters = count_letters(book_text)
    print(number_of_letters)

def count_letters(book_text):
    character_dict = {}
    low_book_text = book_text.lower()
    for character in low_book_text:
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    return character_dict

def count_words(book_text):
    words_in_text = book_text.split()
    return len(words_in_text)


def  read_the_book(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

main()