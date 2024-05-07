def main():
    filepath = "books/frankenstein.txt"

    file_contents = get_book_text(filepath)
    word_count = count_words(file_contents)
    letter_count_dict = count_letters(file_contents)
    letter_count_list = convert_dict_to_list_of_dict(letter_count_dict)

    print("welcome to bookbot!")
    print("-----------------------------------------------------------------------")
    print(f"report for book {filepath}:")
    print()
    print("------------ START OF REPORT ------------")
    print(f"{word_count} words found in book!")
    print()
    print("Here are the amount of times different letters appeared in the book:")
    print("Sort order: descending")
    print()

    for d in letter_count_list:
        print(f"The letter '{d['name']}' appears {d['num']} times!")

    print()
    print("------------- END OF REPORT -------------")


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


def convert_dict_to_list_of_dict(dictionary):
    count_list = []

    for key in dictionary.keys():
        count_list.append(
                {
                    "name": key,
                    "num": dictionary[key]
                }
            )

    count_list.sort(reverse=True, key=sort_chars_on)

    return count_list


def sort_chars_on(d):
    return(d["num"])


main()
