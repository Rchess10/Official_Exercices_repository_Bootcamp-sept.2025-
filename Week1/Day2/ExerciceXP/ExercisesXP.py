#Exercice1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
future_dic = {}
for key, value in zip(keys, values):
    future_dic[key] = value
print(future_dic)

#Exercice2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0

for name, age in family.items():
    if age < 3: 
        price = 0
        print (f"Entrance is free for {name}")
        total_cost += price
    elif 3 <= age <= 12:
        price = 10
        print (f"Please pay {price}$ m.{name}")
        total_cost += price
    else:
        price = 15
        print (f"Please pay {price}$ m.{name}")
        total_cost += price

print(f'total cost: {total_cost}')

#Exercice 3
Brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# Change the value of number_stores to 2
Brand["number_stores"] = 2

# Print a sentence describing Zara’s clients using the type_of_clothes key
print(f"Zara's clients are: {', '.join(Brand['type_of_clothes'])}.")

# Add a new key country_creation with the value Spain
Brand["country_creation"] = "Spain"

# Check if international_competitors exists and, if so, add “Desigual” to the list
if "international_competitors" in Brand:
    Brand["international_competitors"].append("Desigual")

# Delete the creation_date key
del Brand["creation_date"]

# Print the last item in international_competitors
print("Last international competitor:", Brand["international_competitors"][-1])

# Print the major colors in the US
print("Major colors in the US:", Brand["major_color"]["US"])

# Print the number of keys in the dictionary
print("Number of keys in Brand:", len(Brand))

# Print all keys of the dictionary
print("All keys in Brand:", list(Brand.keys()))



#Exercise4 

def describe_city(city, country="Unknown"):
    print(f'{city} is in {country}')

describe_city("Paris", "France")
describe_city("paris")



#Exercise 5: Random

import random 
def rand_number(number):
     rand_num = random.randint(1, 100) 
     if number == rand_num:
        print(f'Success!')
     else: 
        print (f'Failed your number was {number} and the bots was {rand_num}')

rand_number(87)

# Exercise 6: Personalized Shirts


def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")


make_shirt()  # Large shirt, default message
make_shirt("medium")  # Medium shirt, default message
make_shirt("small", "Custom message")  # Small shirt, custom message


make_shirt(size="small", text="Hello!")


# Exercise 7: Temperature Advice

def get_random_temp():
    # Return a random integer between -10 and 40
    return random.randint(-10, 40)

def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don't forget your coat.")
    elif 17 <= temp <= 23:
        print("Nice weather.")
    elif 24 <= temp <= 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")

main()

import random
def get_random_temp():
    return random.randint(-10,40)

def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
    
    if temp < 1: 
        print(f"Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp <= 16: 
            print("Quite chilly! Don't forget your coat.")
    elif 17 <= temp <= 23:
        print("Nice weather.")
    elif 24 <= temp <= 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")
main()

#  Exercise 8: Pizza Toppings

ingredient = []
final_price = 10 
while True: 
    added_by_you = input("Enter your topping: ")
    if added_by_you == "I quit":
        break 
    ingredient.append(added_by_you)
    final_price += 2.5
    print(f"Adding {added_by_you} to your pizza.")

print(f'the final price of your pizza is {final_price}')