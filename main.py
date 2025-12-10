def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = num_words(text)
    print(f"Found {count} total words.")


def get_book_text(path):
    with open(path) as f:
        return f.read()
def num_words(text):
    words = text.split()
    return len(words)    

main()