# ------------------------------
# Python Dictionaries Course
# ------------------------------

# Introduction:
# Un dictionnaire est une collection non ordonnée d'éléments stockés sous forme de paires clé-valeur.
# Il est mutable et dynamique, ce qui signifie qu'on peut modifier, ajouter ou supprimer des éléments.

# Définition d'un dictionnaire
my_dict = {
    'first_name': 'Rick',
    'last_name': 'Sanchez'
}
# Les clés sont des chaînes de caractères, les valeurs peuvent être de n'importe quel type.

# Accès aux données
print(my_dict['first_name'])  # Affiche 'Rick'
# Si la clé n'existe pas, une erreur KeyError est levée.

# Exemple de dictionnaire plus complexe
my_dog = {
    'name': 'Rufus',
    'age': 4,
    'good_dog': True,
    'best_friend': {
        'name': 'Felix',
        'age': 4.5
    },
    'favorite_foods': ['steaks', 'sausages', 'shawarma']
}
print(my_dog['best_friend']['name'])  # Accès à un dictionnaire imbriqué

# Différence avec les listes
my_list = ['Rick', 'Sanchez']
print(my_list[1])  # Accès par index
print(my_dict['last_name'])  # Accès par clé

# Opérations sur les dictionnaires
# Modifier une valeur
my_dict['last_name'] = 'SANCHEZ'
# Ajouter une nouvelle clé
my_dict['hair_color'] = 'white'
# Supprimer une clé
del my_dict['hair_color']

# Restrictions sur les clés
# Les clés doivent être uniques et immuables (str, int, float, bool, tuple)
# Les listes ne peuvent pas être des clés.

# Vérifier la présence d'une clé
print('first_name' in my_dict)  # True

# Itérer sur un dictionnaire
for key in my_dict:
    print(key, my_dict[key])

# Itérer sur les paires clé-valeur
for key, value in my_dict.items():
    print(key, '->', value)

# Méthodes intégrées
print(my_dict.keys())    # Toutes les clés
print(my_dict.values())  # Toutes les valeurs
print(my_dict.items())   # Toutes les paires clé-valeur

# Mise à jour d'un dictionnaire
update_dict = {'first_name': 'Morty', 'hair_color': 'brown'}
my_dict.update(update_dict)
print(my_dict)

# Dictionnaires dans des listes
shirts = [
    {'name': 'Awesome T-shirt 3000', 'size': 'S', 'price': 20},
    {'name': 'Awesome T-shirt 3000', 'size': 'M', 'price': 25},
    {'name': 'Awesome T-shirt 3000', 'size': 'L', 'price': 30}
]
for shirt in shirts:
    print(shirt['size'])

# Challenge: Accéder à une valeur imbriquée
sample_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}


print(sample_dict["class"]["student"]["marks"]["history"]) # Affiche 80

for marks in sample_dict:
    print(sample_dict["class"]["student"]['marks']) #Affiche {'physics': 70, 'history': 80}

for value in sample_dict["class"]["student"]["marks"].values(): #Affiche 70 80
    print(value)

# Ajout d'une clé 'email' dans le dictionnaire imbriqué 'student'
sample_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

sample_dict["class"]["student"]["email"] = "mike@email.com"
print(sample_dict["class"]["student"])

# Résultat : {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}, 'email': 'mike@email.com'}

# Challenge: Supprimer des clés d'un dictionnaire
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys_to_remove = ["name", "salary"]

del sample_dict  ["name"] #to delete one item 
del sample_dict (["name"], ["salary"]) #to delete two item 
for key in keys_to_remove: #to delete using loop
    sample_dict.pop(key)

print(sample_dict)  # Affiche {'age': 25, 'city': 'New york'}

# Conclusion:
# Les dictionnaires sont essentiels pour manipuler efficacement des données en Python.
# Ils sont utilisés dans l'analyse de données, le développement web, et partout où un accès rapide à des valeurs est nécessaire.