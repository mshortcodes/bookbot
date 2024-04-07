def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count_dict = get_letter_count(text)
    sorted_list = convert_to_sorted_list(letter_count_dict)

    print(f"--- Begin report of {book_path} ---\n")
    print(f"{word_count} words found in the document\n")

    for dict in sorted_list:
        print(f"The letter '{dict["char"]}' was found {dict["num"]} times")

    print("\n--- End report ---")

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def get_word_count(text):
    word_list = text.split()
    word_count = len(word_list)
    return word_count

def get_letter_count(text):
    letter_count = {}
    for letter in text:
        letter = letter.lower()
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def convert_to_sorted_list(dict):
    sorted_list = []
    for key in dict:
        if key.isalpha():
            value = dict[key]
            sorted_list.append({"char": key, "num": value})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]

main()