from stats import num_of_words
from stats import num_of_char
from stats import sorted_list_dict

def main():

    file_path = "books/frankenstein.txt"

    num_words = num_of_words(file_path)
    print(f"Found {num_words} total words")

    num_chars = num_of_char(file_path)
    print(num_chars)

    sorted_list = sorted_list_dict(file_path)

main()