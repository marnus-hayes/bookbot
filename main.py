def main():
    filepath = "books/frankenstein.txt"
    file_contents = get_book_text(filepath)
    word_count = count_words(file_contents)
    print(f"{word_count} words found in book!")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(text):
    word_list = text.split()
    return len(word_list)

main()
