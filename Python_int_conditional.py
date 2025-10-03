# amount_bank = 1000
# car = 3000
# username = input("Enter your name: ")

# if username == "Jhon":
#     print ("Welcome Jhon!")
# else :
#     print ("I don't know you.")

# if amount_bank >= car:
#     print ("You can buy the car.")
#     amount_bank -= car
#     print ("You have " + str(amount_bank) + " left in your bank account.")
# else :
#     print ("You cannot buy the car.")
#     print ("You need " + str(car - amount_bank) + " more to buy the car.")

# amount_second_bank = 2000
# price_car = 3000
# price_scooter = 1000

# if amount_second_bank >= price_car:
#     print ("You can buy the car.")
#     amount_second_bank -= price_car
#     print ("You have " + str(amount_second_bank) + " left in your bank account.")
# elif amount_second_bank >= price_scooter:
#     print ("You can buy the scooter.")
#     amount_second_bank -= price_scooter
#     print ("You have " + str(amount_second_bank) + " left in your bank account.")
# else :
#     print ("You cannot buy the car or the scooter.")
#     print ("You need " + str(price_scooter - amount_second_bank) + " more to buy the scooter.")

# #the number of elif isn't limited 

# height = 140 
# age = 10 
# name = "Mickey"

# if height >= 145 or name == "Mickey" and age >= 8:
#     print ("You can go on the ride.")
# else:
#     print ("You cannot go on the ride.")

# List: ordered, mutable, allows duplicates
fruits_list = ["apple", "banana", "orange", "apple"]
print("List:", fruits_list)
#compter le nombre d"éléments dans une liste
print("Number of elements in the list:", len(fruits_list))

# Tuple: ordered, immutable, allows duplicates
fruits_tuple = ("apple", "banana", "orange", "apple")
print("Tuple:", fruits_tuple)

# Set: unordered, mutable, no duplicates
fruits_set = {"apple", "banana", "orange", "apple"}
print("Set:", fruits_set)

# Dictionary: key-value pairs, keys must be unique
fruits_dict = {"red": "apple", "yellow": "banana", "orange": "orange"}
print("Dictionary:", fruits_dict)

#avec la méthode for
for fruit in fruits_list:
    print(f"je mange une/un {fruit} tous les jours")

#avec la méthode range
for i in range(len(fruits_list)):
    print(f"je mange une/un {fruits_list[i]} tous les jours")

#table de multiplication de 5
for i in range(11):
    multiplication = f"{i} * 5 "
    result = i * 5
    sentence = f"{multiplication} = {result}"
    print (sentence)

animals_farm = ["cat", "dog", "cow", "sheep"]

for animal in animals_farm:
    print(f"i have a {animal} in my farm")