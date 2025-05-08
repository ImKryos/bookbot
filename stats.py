def get_num_words(path_to_file):
    word_list = get_book_text(path_to_file).split()
    return len(word_list)
    

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def char_count(path_to_file):
    text = get_book_text(path_to_file).lower()
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_on(dict):
    return dict["num"]

def sort_char_count(counts_dict):
    char_list = []
    for char, count in counts_dict.items():
        char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

    
