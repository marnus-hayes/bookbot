def main():
    filepath = "books/frankenstein.txt"

    file_contents = get_book_text(filepath)
    word_count = count_words(file_contents)
    letter_count = count_letters(file_contents)

    print(f"{word_count} words found in book!")
    print("Here are the amount of times different letters appeared in the book:")
    print(letter_count)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(text):
    word_list = text.split()
    return len(word_list)

def count_letters(text):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    lowercase_text = text.lower()
    letters = list(lowercase_text)
    counts = {}

    for letter in letters:
        if letter in alphabet:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 0
    return counts



main()
