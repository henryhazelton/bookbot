def count_words(book_text):
    words_in_text = book_text.split()
    return len(words_in_text)

def count_letters(book_text):
    character_dict = {}
    low_book_text = book_text.lower()
    for character in low_book_text:
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    return character_dict