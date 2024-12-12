def main():
    with open('books/frankenstein.txt') as file:
        book_contents = file.read()
    num_words = get_word_count(book_contents)
    char_count = get_char_count(book_contents)
    sorted_char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} found in the document\n")
    for char in sorted_char_count:
        print(f"The '{char}' character was found {sorted_char_count[char]} times")
    print(f"--- End report ---")


def get_word_count(book):
    return len(book.split())


def get_char_count(book):
    char_count_dit = {}
    for char in book:
        lower_case_char = char.lower()
        if lower_case_char.isalpha():
            if lower_case_char not in char_count_dit:
                char_count_dit[lower_case_char] = 1
            else:
                char_count_dit[lower_case_char] += 1
    return char_count_dit


if __name__ == '__main__':
    main()
