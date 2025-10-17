from stats import num_of_words
from stats import num_of_char
from stats import sorted_list_dict

def main():

    file_path = "books/frankenstein.txt"

    sorted_list = sorted_list_dict(file_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    num_words = num_of_words(file_path)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        if dict["char"].isalpha():
            first = dict["char"]
            second = dict["num"]
            print(f"{first}: {second}")
    
main()