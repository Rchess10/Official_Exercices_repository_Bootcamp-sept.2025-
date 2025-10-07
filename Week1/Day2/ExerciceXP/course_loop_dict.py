# ------------------------------
# Cours : Boucles et Dictionnaires en Python
# ------------------------------

# Introduction :
# Ce cours combine la puissance des boucles avec la flexibilité des dictionnaires,
# pour traiter et manipuler efficacement des paires clé-valeur en Python.

# Ce que vous allez apprendre :
# - Parcourir un dictionnaire avec différentes techniques de boucle.
# - Utiliser les instructions break, continue et pass dans les boucles.
# - Intégrer les clauses else avec les boucles for et while.
# - Utiliser range, enumerate et zip pour enrichir les boucles.

# Prérequis :
# - Connaissance de base de la syntaxe Python.
# - Compréhension des structures de données, notamment les dictionnaires.
# - Savoir utiliser les boucles for et while.

# Ressources utiles :
# - Boucles for avec dictionnaires en Python
# - Boucles for avec else en Python

# Parcourir un dictionnaire
my_books = {
    "title": "Harry Potter",
    "author": "JK Rowling",
}

for x, y in my_books.items():
    print(f"Le {x} est {y}")
# Résultat :
# Le title est Harry Potter
# Le author est JK Rowling

# Opérateurs de boucle

# range(start, stop[, step]) : crée un itérable pour les boucles
print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]

# enumerate(iterable) : énumère chaque élément avec son index
for item in enumerate('abcd'):
    print(item)
# (0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')

for index_count, letter in enumerate('abcd'):
    print(f"A l'index {index_count} la lettre est {letter}")

# zip(iterable, ...) : regroupe plusieurs listes en tuples
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [1.1, 2.2, 3.3, 4.4, 5.5]
for item in zip(list1, list2, list3):
    print(item)
# (1, 'a', 1.1), (2, 'b', 2.2), (3, 'c', 3.3)

# For Else
for i in range(1, 3):
    print(i)
else:
    print('La boucle for est terminée')
# 1, 2, La boucle for est terminée

# While Else
x = 0
while x < 2:
    print(f'x vaut {x}')
    x += 1
else:
    print('x est supérieur ou égal à 2')
# x vaut 0, x vaut 1, x est supérieur ou égal à 2

# Break, Continue, Pass

# break : arrête la boucle
for letter in 'Leonardo':
    if letter == 'a':
        break
    print(letter, end='')  # Affiche Leon

# continue : passe à l'itération suivante
for letter in 'Leonardo':
    if letter == 'o':
        continue
    print(letter, end='')  # Affiche Lenard

# pass : ne fait rien (utile pour des blocs vides)
for item in [1, 2, 3]:
    pass
print('Fin du script')

# Challenge 🚀
# Implémentez une boucle qui demande à l'utilisateur d'ajouter des entrées dans un dictionnaire
# jusqu'à ce qu'il saisisse 'quit'. Affichez le dictionnaire final.

user_dict = {}
while True:
    key = input("Entrez une clé (ou 'quit' pour arrêter) : ")
    if key == 'quit':
        break
    value = input("Entrez la valeur : ")
    user_dict[key] = value
print("Votre dictionnaire :", user_dict)

# Conclusion :
# Vous savez maintenant combiner boucles et dictionnaires pour manipuler dynamiquement des données.
# Ces compétences vous aideront à créer des applications Python interactives et efficaces.

for index_count, letter in enumerate('abcd'):
    print("A l'index {} la lettre est {}".format(index_count, letter)) 

# enumerate('abcd') :
# Cette fonction retourne un itérable de tuples contenant l’index et la lettre pour chaque caractère de la chaîne 'abcd'.
# Par exemple, le premier tuple est (0, 'a'), le second (1, 'b'), etc.

# for index_count, letter in enumerate('abcd') :
# À chaque tour de boucle, index_count prend la valeur de l’index (0, puis 1, puis 2, puis 3) et letter prend la lettre correspondante ('a', 'b', 'c', 'd').

# print("A l'index {} la lettre est {}".format(index_count, letter)) :
# Ici, la méthode .format() permet d’insérer les valeurs de index_count et letter dans la chaîne à la place des accolades {}.
# Par exemple, pour le premier tour, cela affiche :
# A l'index 0 la lettre est a

# Focus sur .format :

# .format() est une méthode des chaînes de caractères qui permet de remplacer les {} par les valeurs passées en argument.
# L’ordre des arguments dans .format() correspond à l’ordre des {} dans la chaîne.
# Cela rend le texte dynamique et lisible, surtout quand on veut afficher des variables dans une phrase.
# Résultat final :
# A l'index 0 la lettre est a
# A l'index 1 la lettre est b
# A l'index 2 la lettre est c
# A l'index 3 la lettre est d
# Chaque ligne affiche l’index et la lettre correspondante, grâce à la méthode .format().

