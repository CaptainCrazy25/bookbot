
def count_words(booktext):
    num_words = len(booktext.split())
    return num_words
def count_letters(booktext):
    lower_case_text = booktext.lower()
    counting_dict = {}
    for letter in lower_case_text:
        if letter in counting_dict:
            counting_dict[letter] += 1
        else:
            counting_dict[letter] = 1
    return counting_dict
def sort_key(char):
    return char["num"]

def sorted_list(counting_dict):
    character_list = []
    for char in counting_dict:
        num = counting_dict[char]
        char = {"char": char, "num": num}
        character_list.append(char)
    character_list.sort(reverse=True, key=sort_key)
    return character_list