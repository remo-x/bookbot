from stats import *
import sys
def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book = get_book_text(file_path)
    word_count = split_function(book)
    char_count = count_characters(book)
    new_dict = sorted_dictionary(book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in new_dict:
        print(item["char"], ":", item["num"])
    print("============= END ===============")

main()


