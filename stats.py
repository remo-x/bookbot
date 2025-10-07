
def split_function(book):
    return len(book.split())

def count_characters(book):
    character_count = {}
    lower_case = book.lower()
    for char in lower_case:
        if char not in character_count:
            character_count[char] = 1
        else:
            character_count[char] += 1
    return character_count


def sort_on(item):
    return item["num"]


def sorted_dictionary(book):
    sorted_dict = []
    character_count = count_characters(book)
    for ch in character_count:
        cnt = character_count[ch]
        if ch.isalpha():
            sorted_dict.append({"char":ch,"num":cnt})
    sorted_dict.sort(reverse=True, key=sort_on)

    
    return sorted_dict



