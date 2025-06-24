from stats import count_words
from stats import count_letters
from stats import sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content   

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
    
        booktext = get_book_text(sys.argv[1])
        num_words = count_words(booktext)
        answer_num_words = f"{num_words} words found in the document"
        answer_counting_letters = count_letters(booktext)
        sorted_letters = sorted_list(answer_counting_letters)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char in sorted_letters:
            if char["char"].isalpha():
                print(f"{char["char"]}: {char["num"]}")


        print("============= END ===============")
main()
