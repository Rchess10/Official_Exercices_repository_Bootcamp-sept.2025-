fruit = ("banana", "apple", "orange" )
print (fruit [-1]) #print the second fruit of the list


number = {101, 102, 103, 101}
number_micro = list(number)
print(number_micro[-1]) # Affiche le dernier élément de la liste

number_set = {5, 10, 15, 20}
number_list = list(number_set)
print("Last element:", number_list[-0])  # Print the last index of the list converted from set

Users_details = {
    "name": "Alice",
    "age": 45,
    "living_location": "New-York"
}

print(f"{Users_details['name']} is {Users_details['age']} years old and lives in {Users_details['living_location']}.")
