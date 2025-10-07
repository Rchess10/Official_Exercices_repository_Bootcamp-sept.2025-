# --- Introduction ---
# Ce cours explore la programmation fonctionnelle en Python :
# lambda, map, filter, reduce.
# Ces outils permettent d'écrire du code plus concis, efficace et prévisible.

# --- What you will learn ---
# - Utiliser map() pour appliquer une fonction à chaque élément d'un itérable.
# - Utiliser filter() pour filtrer les éléments selon une condition.
# - Utiliser reduce() pour réduire une séquence à une seule valeur.
# - Créer et utiliser des fonctions lambda pour des opérations rapides.

# --- Prérequis ---
# - Savoir utiliser les fonctions Python.
# - Être à l'aise avec les listes et dictionnaires.

# --- Ressources ---
# - https://www.programiz.com/python-programming/methods/built-in/map
# - https://realpython.com/python-map-function/
# - https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions

# # --- La fonction map() ---
# def upper_string(s):
#     return s.upper()

# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# map_object = map(upper_string, fruit)
# print(list(map_object))  # ['APPLE', 'BANANA', 'PEAR', 'APRICOT', 'ORANGE']

# # map applique upper_string à chaque fruit et retourne les résultats.

# # --- La fonction filter() ---
# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# def starts_with_A(s):
#     return s[0] == "A"

# filtered_object = filter(starts_with_A, fruit)
# print(list(filtered_object))  # ['Apple', 'Apricot']

# # filter garde uniquement les éléments qui commencent par "A".

# # --- La fonction functools.reduce() ---
# from functools import reduce

# def sum_numbers(first, second):
#     return first + second

# my_list = [1, 3, 5, 7]
# reduced_list = reduce(sum_numbers, my_list)
# print(reduced_list)  # 16

# reduce applique sum_numbers cumulativement à la liste.

# --- Les fonctions lambda ---
# Une lambda est une fonction anonyme, écrite sur une ligne.
# Syntaxe : lambda arg1, arg2: valeur_retournée

# # Exemple simple :
# print((lambda s: s.upper())("banana"))  # 'BANANA'
# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]

# # On peut aussi stocker une lambda :
# my_function = lambda s: s.upper()
# print(my_function("pear"))  # 'PEAR'
# from functools import reduce
# my_list = [1, 3, 5, 7]

# # Utilisation avec map, filter, reduce :
# print(list(map(lambda s: s.upper(), fruit)))  # ['APPLE', 'BANANA', 'PEAR', 'APRICOT', 'ORANGE']
# print(list(filter(lambda s: s[0] == "A", fruit)))  # ['Apple', 'Apricot']
# print(reduce(lambda first, second: first + second, my_list))  # 16

# # --- Challenge 🚀 ---
# people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
# hello_people = map(lambda name: f"Hello {name}!", filter(lambda name: len(name) <= 4, people))
# print(list(hello_people))  # ['Hello Rick!', 'Hello Beth!']

# people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
# hello_people = list(filter(lambda s:len(s) <= 4, people))
# print(hello_people)


# # --- Conclusion ---
# # Les fonctions lambda, map, filter et reduce sont des outils puissants pour écrire du code Python concis et lisible.
# # Elles facilitent la programmation fonctionnelle et permettent de manipuler facilement des collections de données.

# # © 2025 Paris School of Technology and Business. All Rights Reserved.