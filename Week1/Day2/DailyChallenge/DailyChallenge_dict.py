# user_word = input("Choose a word: ")
# letters_dict = {}

# for index, letter in enumerate(user_word): 
#      letters_dict[letter] = index

# print(letters_dict)
# print(index)


user_word = input("Choose a word: ")
letters_dict = {}


for index, letter in enumerate(user_word):
    # Make sure the letter is a string (always true for characters in a string)
    # If the letter is not already a key, create a new list for it
    if letter not in letters_dict:
        letters_dict[letter] = []
    # Append the current index to the list for this letter
    letters_dict[letter].append(index)

# Print the resulting dictionary
print(letters_dict)
