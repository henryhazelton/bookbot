def main():
    book_path = "books/frankenstein.txt"
    book_text = read_the_book(book_path)
    print(book_text)
    
def  read_the_book(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents
main()