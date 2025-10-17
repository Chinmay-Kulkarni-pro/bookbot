import sys
from stats import num_of_words
from stats import sorted_list_dict

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    file_path = sys.argv[1]

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