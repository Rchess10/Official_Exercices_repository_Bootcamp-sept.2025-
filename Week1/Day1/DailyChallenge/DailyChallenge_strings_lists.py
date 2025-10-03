#Challenge 1
number = input("Enter a number: ")
length = input("Enter the length of the number: ")

multiples = []
for i in range(1, int(length) + 1):
    multiples.append(i * int(number))

print(multiples)

#Challenge 2
user_word = input("Enter a word: ")

result  = ""
for letter in user_word:
    if not result or letter != result[-1]:
        result += letter
print(result)