#Exercie1
class Cat: 
    def __init__(self, name, age):
         self.name = name 
         self.age = age 

cat1 = Cat("Chouppy", 15)
cat2 = Cat("Grouppy", 12)
cat3 = Cat("Souppy", 20)

def find_oldest(cat1, cat2, cat3):
    if cat1.age >= cat2.age and cat1.age >= cat3.age:
        oldest_cat = cat1
    elif cat2.age >= cat1.age and cat2.age >= cat3.age:
        oldest_cat = cat2
    else:
        oldest_cat = cat3
    return oldest_cat


oldest_cat = find_oldest(cat1,cat2, cat3)
print(f"{oldest_cat.name} becasue its age was {oldest_cat.age}")


# # Other method
# def find_old(cat1, cat2, cat3):
#     oldest = max([cat1,cat2,cat3], key = lambda cat : cat.age)
#     return oldest 

# oldest_cat = find_old(cat1, cat2, cat3)
# print(f"{oldest_cat.name} because its age is {oldest_cat.age}")

#Exercice2
class Dog: 
    def __init__(self, name, height):
        self.name = name
        self.height = height 

    def bark(self):
        print(f'{self.name} goes woof!')

    def jump(self): 
        print(f'{self.name} jumps {int(self.height)*2} cm high!')

davids_dog = Dog("wolfy","120")
sara_dog = Dog("malinois","140")

print(f'{davids_dog.name} and {davids_dog.height}')
print(f'{sara_dog.name} and {sara_dog.height}')

davids_dog.bark()
davids_dog.jump()

sara_dog.bark()
sara_dog.jump()

#Exercie3
class song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def singmeasong(self):
        for onebyone in self.lyrics:
            print(onebyone)

stairway = song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.singmeasong()

#Exercice 4
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
        self.groups = {}

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} has been added to the zoo.")

    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold/retired from the zoo.")
        else:
            print(f"{animal_sold} not found in the zoo.")

    def sort_animals(self):
        self.groups = {}
        for animal in sorted(self.animals):
            first_letter = animal[0].upper()
            if first_letter not in self.groups:
                self.groups[first_letter] = [animal]
            else:
                self.groups[first_letter].append(animal)

    def get_groups(self):
        print("Grouped animals:")
        for letter, animals in self.groups.items():
            print(f"{letter}: {animals}")

# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal("Cat")
brooklyn_safari.add_animal("Cougar")
brooklyn_safari.add_animal("Lion")
brooklyn_safari.add_animal("Zebra")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()