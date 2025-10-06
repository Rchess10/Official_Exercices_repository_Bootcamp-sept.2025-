#Challenge1
number = input("Enter a number: ")
length = input("Enter the length of the number: ")

multiples = []
for i in range(1, int(length) + 1):
    multiples.append(i * int(number))

print(multiples)

#Challenge1_var

num = int(input("enter a num:"))
lenght = int(input("enter a lenght:"))
multiples = [i * num for i in range(1, lenght + 1)]

# for num = 3 and lenght = 5
# [i * 3 for i in range(1, 5 +1)]

print(multiples)


#Challenge 2
user_word = input("Enter a word: ")

result  = ""

for letter in user_word:
    if not result or letter != result[-1]:
        result += letter
print(result)

#Challenge 2_var
user_inut = (input("enter a word:"))
result = user_inut[0]

for i in range (1, len(user_inut)):
    if user_inut[i] != user_inut[i - 1]: # != means different
        result += user_inut[i]

print(result)