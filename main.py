import sys
from stats import get_num_words, get_book_text, char_count, sort_char_count

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_file = sys.argv[1]

print("============ BOOKBOT ============")
print(f"Analyzing book found at {path_to_file}...")
print("----------- Word Count ----------")
print(f"Found {get_num_words(path_to_file)} total words")
print("--------- Character Count -------")
counts = char_count(path_to_file)
sorted_counts = sort_char_count(counts)
for item in sorted_counts:
    if item['char'].isalpha():
        print(f"{item['char']}: {item['num']}")
print("============= END ===============")
