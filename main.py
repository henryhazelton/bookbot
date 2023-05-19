def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters_dictionary = get_characters_dictionary(text)
    characters_sorted_list = characters_dictionary_to_sorted_list(characters_dictionary)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in characters_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def characters_dictionary_to_sorted_list(number_characters_dictionary):
    sorted_list = []
    for ch in number_characters_dictionary:
        sorted_list.append({"char": ch, "num": number_characters_dictionary[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_characters_dictionary(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_character_sums(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()