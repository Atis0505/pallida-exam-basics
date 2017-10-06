# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases

def unique_characters(input_string):
    letters_dict = {}
    for letter in input_string:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
    unique_char_list = []
    unique_chars_list = [letter for letter, value in letters_dict.items() if value == 1]
    if len(input_string) == 0:
        return False
    else:
        return unique_chars_list

print(unique_characters("anagram"))
# Should print out:
# ["n", "g", "r", "m"]


