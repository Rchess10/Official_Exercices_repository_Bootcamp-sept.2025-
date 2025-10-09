# class Animal():
#     def __init__(self, type, number_legs, sound):
#         self.type = type
#         self.number_legs = number_legs
#         self.sound = sound

#     def make_sound(self):
#         print(f"I am an animal, and I love saying {self.sound}")

# class Dog(Animal):
#     pass

# rex= Dog("dog", 4, "wouaf")
# print('This animal is a:', rex.type)
# # >> This animal is a dog

# print('This dog has', rex.number_legs , ' legs')
# # >> This dog has 4 legs

# print('This dog makes the sound ', rex.sound)
# # >> This dog makes the sound wouaf

# rex.make_sound()

###################################################################
# class Animal():
#     def __init__(self, type, number_legs, sound):
#         self.type = type
#         self.number_legs = number_legs
#         self.sound = sound

#     def make_sound(self):
#         print(f"I am an animal, and I love saying {self.sound}")

# class Dog(Animal):
#     def fetch_ball(self):
#         print("I am a dog, and I love fetching balls")

# rex = Dog('dog', 4, "Wouaf")
# print('This animal is a:', rex.type)
# # >> This animal is a dog

# rex.fetch_ball()
# # >> I am a dog, and I love fetching balls

# roger = Animal('Roger', 4, "Grr")
# roger.fetch_ball()
# # >> AttributeError: 'Animal' object has no attribute 'fetch_ball'

#############################################################

# class Circle:
#     color = "red"

# class NewCircle(Circle):
#     color = "blue"

# nc = NewCircle
# print(nc.color)
# # >> What will be the output ?

############################################################

# class Circle: # Définition de la classe "Circle" (Cercle)
#     def __init__(self, diameter): # Méthode spéciale (constructeur) appelée lors de la création d'un objet Circle. 'self' fait référence à l'objet lui-même, 'diameter' est le diamètre initial passé en paramètre.
#       self.diameter = diameter # On stocke la valeur du 'diameter' passé dans un attribut de l'objet, également appelé 'diameter'.
#                                # self.diameter représente le diamètre *de cet objet Circle spécifique*.

#     def grow(self, factor=2): # Définition d'une méthode 'grow' (grandir) pour la classe Circle.
#                               # 'self' fait référence à l'objet. 'factor' est un multiplicateur, avec une valeur par défaut de 2.
#         """grows the circle's diameter by factor""" # Une docstring (description) de la méthode.
#         self.diameter = self.diameter * factor # Le diamètre de l'objet est multiplié par le 'factor'.
#                                                # Ex: Si self.diameter était 1 et factor 2, il devient 1 * 2 = 2.

# class NewCircle(Circle): # Définition de la classe "NewCircle" (Nouveau Cercle).
#                          # Entre parenthèses '(Circle)', cela indique que NewCircle hérite de Circle.
#                          # NewCircle possède donc toutes les méthodes et attributs de Circle par défaut,
#                          # à moins qu'elle ne les redéfinisse.

#     def grow(self, factor=2): # NewCircle redéfinit sa propre méthode 'grow'.
#                               # C'est ce qu'on appelle la surcharge (override) : cette version de 'grow' sera utilisée
#                               # pour les objets NewCircle, et non celle de la classe parente Circle.
#         """grows the area by factor...""" # Nouvelle docstring expliquant que cette version est différente.
#         self.diameter = (self.diameter * factor * 2) # Nouvelle logique de croissance :
#                                                      # le diamètre est multiplié par 'factor' ET par 2.
#                                                      # C'est la ligne clé qui change le comportement.

# nc = NewCircle(1) # LIGNE 1 : Création d'un objet 'nc' (notre "nouveau cercle").
#                   # On appelle le constructeur de NewCircle (qui est celui de Circle ici).
#                   # self.diameter est initialisé à 1.
#                   # Valeurs actuelles : nc.diameter = 1

# print(nc.diameter) # LIGNE 2 : Affichage de la valeur de l'attribut 'diameter' de l'objet 'nc'.
#                    # Valeurs actuelles : nc.diameter = 1
#                    # Output : 1

# nc.grow() # LIGNE 3 : Appel de la méthode 'grow' sur l'objet 'nc'.
#           # Python cherche la méthode 'grow' dans NewCircle d'abord (car 'nc' est un NewCircle).
#           # Il trouve la version de NewCircle : def grow(self, factor=2).
#           # 'factor' n'est pas fourni, donc il prend sa valeur par défaut : factor = 2.
#           # La ligne exécutée est : self.diameter = (self.diameter * factor * 2)
#           # On remplace les valeurs : nc.diameter = (1 * 2 * 2)
#           # nc.diameter devient 4.
#           # Valeurs actuelles : nc.diameter = 4

# print(nc.diameter) # LIGNE 4 : Affichage de la nouvelle valeur de l'attribut 'diameter' de l'objet 'nc'.
#                    # Valeurs actuelles : nc.diameter = 4
#                    # Output : 4
# # >> What will be the output (Quel sera le résultat)

# # Résultat final attendu du programme :
# # 1
# # 4

#############################################################

# class Animal():
#     def __init__(self, type, number_legs, sound):
#         self.type = type
#         self.number_legs = number_legs
#         self.sound = sound

# class Dog(Animal):
#     def __init__(self, type, number_legs, sound, fetch_ball):
#         super().__init__(type, number_legs, sound)
#         # Or : Animal.__init__(self,type, number_legs, sound)
#         self.fetch_ball = fetch_ball

# rex = Dog('dog', 4, "wouaf", True)
# print('This animal is a:', rex.type)
# # >> This animal is a dog

# print('This dog has', rex.number_legs , ' legs')
# # >> This dog has 4 legs

# print('This dog makes the sound ', rex.sound)
# # >> This dog makes the sound wouaf

# print('Does this dog fetchs balls ? ', rex.fetch_ball)
# # >> Does this dog fetchs balls ? True

############################################################

# from faker import Faker
# fake = Faker()
# print(fake.date())

