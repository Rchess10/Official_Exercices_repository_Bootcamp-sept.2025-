#Daily challenge one

user_word = input("Choose a word: ")
letters_dict = {}


for index, letter in enumerate(user_word):
    # If the letter is not already a key, create a new list for it
    if letter not in letters_dict:
        letters_dict[letter] = []
    # Append the current index to the list for this letter
    letters_dict[letter].append(index)

# Print the resulting dictionary
print(letters_dict)
