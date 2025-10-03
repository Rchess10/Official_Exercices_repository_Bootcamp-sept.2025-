animal_farm_list = ["cat", "dog", "cow", "sheep"]

for i in range(len(animal_farm_list)):
    animal_farm_list[i] = animal_farm_list[i] + "s"
    print(animal_farm_list[i])

print(animal_farm_list)

print(enumerate(animal_farm_list))
list_enumerate = list(enumerate(animal_farm_list))
print(list_enumerate)

list_fruits = ["apple", "banana", ["orange", "apple"]]
fruit_orange = list_fruits[2][0]
print(fruit_orange)

for i, fruit in enumerate(list_fruits):
    print(i, fruit)
    list_fruits[i] = list_fruits[i] + "s"