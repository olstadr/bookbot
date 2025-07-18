# fn accepts text from book as string & returns # of words
def get_num_words(book_text):
    word_counter = 0
    words = book_text.split()
    for word in words:
        word_counter += 1
    return word_counter

def get_character_count(book_text):
    # dictionary keys are str characters, values are int
    characters_dict = {
    }
    book_text_lowercase = book_text.lower()
    for character in book_text_lowercase:
        if character in characters_dict:
            characters_dict[character] += 1
        else:
            characters_dict[character] = 1
    return characters_dict

def get_list_of_dict(characters_dict):
    list_of_dict = []
    for char in characters_dict:
        num = characters_dict[char]
        list_of_dict.append({"char": char, "num": num})
    return list_of_dict

def sort_on(characters_dict):
    return characters_dict["num"]
