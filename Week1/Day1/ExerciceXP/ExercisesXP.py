# #Exercise 1 : Hello World
# for i in range(4): print("Hello World")

# #Exercise 2 : Some Math
# result = 99 ** 3 *8
# print (result)

# #Exercise 3 : What’s your name ?
# my_name = "John"
# username = input("What is your name? ")

# if username == my_name:
#     print(f"Hello {username}, beautiful name by the way!")
# else:
#     print(f"Hello {username}, wrong name I guess")

# #Exercise 4 : Tall enough to ride a roller coaster
# height = int(input("Enter your height in cm: "))
# if height > 145 :
#     print("You are tall enough to ride the roller coaster!")
# else:
#     print("You need to grow taller before you can ride.")

# #Exercise 5 : Favorite Numbers
# my_set_fav_numbers = {7, 42, 3, 55, 78}

# my_set_fav_numbers.add(8)
# my_set_fav_numbers.add(12)

# my_set_fav_numbers.remove(12)

# friend_fav_numbers = {152, 225, 352, 424, 529}

# our_fav_numbers = my_set_fav_numbers.union(friend_fav_numbers)

# print(our_fav_numbers)

# #Exercice 6 : Tuple 
# answer = str(f"Un tuple en Python est une collection ordonnée et immuable d’éléments.Cela signifie que tu ne peux pas modifier, ajouter ou supprimer des éléments après sa création.")
# print(answer)

# #Exercice 7 : List Manipulation
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# basket.count("Apples")
# basket.clear()
# print (basket)

#Exercice 8 : Sandwich Orders
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
finished_sandwiches = []

for i in sandwich_orders:
    if i == "Pastrami sandwich":
        sandwich_orders.remove(i)
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(current_sandwich)
    print(f"I made your {current_sandwich}")