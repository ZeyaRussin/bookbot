def get_num_words(book):
   return len(book.split())

def get_character_amount(book):
    character_dictionary = {}
    for char in book.lower():
        if char in character_dictionary:
            character_dictionary[char] += 1
        else:
            character_dictionary[char] = 1
    return character_dictionary

def sort_on(items):
    return items["num"]

def get_character_list(character_dictionary):
    character_list = []
    for char in character_dictionary:
        character_list.append({"char": char, "num": character_dictionary[char]})
    character_list.sort(reverse=True, key=sort_on)
    return character_list