def get_book_text(file_path):

    with open(file_path) as f:
        file_contents = f.read()    
    return file_contents

def num_of_words(file_path):
    
    book_text_string = get_book_text(file_path)
    book_text_list = book_text_string.split()
    return len(book_text_list) 

def num_of_char(file_path):
    
    book_text_string = get_book_text(file_path)

    book_text_list = list(book_text_string)

    book_text_set = set(book_text_list)
    book_text_set2 = {item.lower() for item in book_text_set}

    book_text_dict = dict.fromkeys(book_text_set2, 0)

    book_text_list2 = [item.lower() for item in book_text_list]

    for char in book_text_list2:
        book_text_dict[char] +=1

    return book_text_dict

def sort_on(items):
    return items["num"]

def sorted_list_dict(file_path):

    my_dict = num_of_char(file_path)

   # Format change from(line 36) -> to(line 37)
   # {"a": 3534, "b": 6 ...}
   # [{"char": "a", "num": 3534},{},...]

    ret_list = []

    #This should give me the entire list of dictionaries in the modified format
    for key in my_dict:
        ret_list.append({"char": key , "num":my_dict[key]})
    
    #Now the sorting
    ret_list.sort(reverse=True, key=sort_on)

    return ret_list
