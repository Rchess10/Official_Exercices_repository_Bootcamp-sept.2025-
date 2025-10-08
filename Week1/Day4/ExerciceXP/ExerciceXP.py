# #Exercice1 Pets 

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'
    
# class Siamese(Cat):
#     def __init__(self, name, age):
#         super().__init__(name,age)
#         self.breed = "Siamese"
#         print(f'my cat is named {name} and his age is {age}, his race is {self.breed}')

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# siam = Siamese("Bengo", 17)
# bengal = Bengal("Milo", 3)
# chartreux = Chartreux("Luna", 4)

# all_cats = [siam, bengal, chartreux]

# print(bengal.name)
# print(chartreux.sing("miaouuuuu"))
# print(list(all_cats))

# sara_pets = Pets(all_cats)
# sara_pets.walk()


#Exercice2 Dogs
# Create a class called Dog with name, age, and weight attributes.
# Implement a bark() method that returns “ is barking”.
# Implement a run_speed() method that returns weight / age * 10.
# Implement a fight(other_dog) method that returns a string indicating which dog won the fight, based on run_speed * weight. 
# import random
# class Dog():

#     def __init__(self, name, age, weight):
#         self.name = name 
#         self.age = age 
#         self.weight = weight

#     def bark(self):
#         return "is barking"
    
#     def run_speed(self):
#         return self.weight / self.age * 10
    
#     def fight(self, other_dog):
#         self_fight_score = self.weight * self.run_speed()
#         other_dog_fight_score = other_dog.weight * other_dog.run_speed()

#         if  self_fight_score > other_dog_fight_score:
#              return f"{self.name} has won the fight"
#         else: 
#              return f"{other_dog.name} has won the fght"
        
# dog1 = Dog("Rex", 5, 20)
# dog2 = Dog("Buddy", 3, 15)
# dog3 = Dog("Luna", 4, 18)

# print(str(dog1.run_speed))
# print(dog1.fight(dog2))
# print(dog1.fight(dog3))



# class Petdog(Dog):
#     def __init__(self, name, age, weight, trained = False):
#         super().__init__(name,age,weight)
#         self.trained = trained
    
#     def train(self):
#         print(self.bark())
#         self.trained = True

#     def play_tog(self, *dogs):
#         print(f"{dogs} all play together")

#     def rand_tricks(self):
#         self.tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
#         if self.trained: # Pas besoin de == True, 'if' suffit pour les booléens
#             # <--- CORRECTION MAJEURE ICI
#             chosen_trick = random.choice(self.tricks)
#             print(f"{self.name} {chosen_trick}!") # L'énoncé semblait attendre "do a [trick]", donc j'ai ajusté

#         else:
#             print(f"{self.name} does nothing because not trained")

        
# p = Petdog("Max", 2, 10)
# ap = Petdog("Loris", 3, 15)
# p.train()
# print(p.trained)
# p.play_tog(p,ap)
# p.rand_tricks()

#Exercie 4
class Person():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name 
        self.last_name = last_name
        self.age = age

    def is_18(self):
        if self.age > 18:
            print("ouf, je le savais")
        else: 
            print("oh merde")

makao = Person("Romain", "Vautey", 17)
makao.is_18()

