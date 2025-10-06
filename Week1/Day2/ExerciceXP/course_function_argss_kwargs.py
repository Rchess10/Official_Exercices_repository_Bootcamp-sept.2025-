# ------------------------------
# Cours : Fonctions, *args et **kwargs en Python
# ------------------------------

# Introduction :
# Une fonction est un bloc de code réutilisable qui s'exécute lorsqu'on l'appelle.
# Les fonctions permettent de structurer, simplifier et réutiliser le code.

# Syntaxe de base
def say_hello():
    """Une fonction qui affiche Hello!"""
    print("Hello!")

say_hello()  # Affiche Hello!

# Définition et appel de fonction avec paramètres
def say_hello(username):
    print("Hello " + username)

say_hello("Rick")   # Hello Rick
say_hello("Morty")  # Hello Morty

# Plusieurs arguments (arguments positionnels)
def say_hello(username, language):
    if language == "EN":
        print("Hello " + username)
    elif language == "FR":
        print("Bonjour " + username)
    else:
        print("Langue non supportée : " + language)

say_hello("Rick", "FR")  # Bonjour Rick

# Arguments nommés (keyword arguments)
say_hello(username="Rick", language="FR")
say_hello(language="FR", username="Rick")  # L'ordre n'a pas d'importance avec les arguments nommés

# Combinaison d'arguments positionnels et nommés
say_hello("Rick", language="FR")  # OK
# say_hello(username="Rick", "FR")  # Erreur

# Valeurs par défaut
def say_hello(username, language="EN"):
    if language == "EN":
        print("Hello " + username)
    elif language == "FR":
        print("Bonjour " + username)
    else:
        print("Langue non supportée : " + language)

say_hello("Rick")  # Hello Rick (par défaut EN)
say_hello("Rick", "FR")  # Bonjour Rick

# Erreurs d'arguments
# say_hello()  # TypeError: il manque des arguments

# Portée locale et globale
def number_by_three(name, day):
    sentence = f'Hello {name}! Today is {day}.'
    print(sentence)

number_by_three ("Romain","Wednesday")
# print(day)  # NameError: day n'est pas défini ici (portée locale)

name = 'Avner'
def say_hi():
    print(name)  # Utilise la variable globale

say_hi()  # Avner

# Valeurs de retour
def get_formatted_name(first_name, last_name):
    """Retourne un nom complet formaté."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)  # Jimi Hendrix

def divide_by_three(number):
    return number / 3

print(divide_by_three(12))  # 4.0
print(divide_by_three(16))  # 9.0

# Retourner plusieurs valeurs avec un tuple
def format_name(first_name, last_name):
    return (first_name.title(), last_name.title())

first, last = format_name("RICk", "mORTY")
print(first)  # Rick
print(last)   # Morty

# Exercice : addition et soustraction
def calculation(a, b):
    return a + b, a - b

res = calculation(40, 10)
print(res)  # (50, 30)

# ------------------------------
# *args et **kwargs
# ------------------------------

# *args : nombre variable d'arguments positionnels
def check_arguments(*args):
    print(f"Voici les arguments : {args}")

check_arguments(1, 2, 'hey')  # (1, 2, 'hey')

def check_multiple_arguments(*args):
    return sum(args)

print(check_multiple_arguments(10, 20, 100, 30))  # 160

# **kwargs : nombre variable d'arguments nommés
def check_keywordedarguments(**kwargs):
    print(kwargs)

check_keywordedarguments(name="Sarah", age=24)  # {'name': 'Sarah', 'age': 24}

def check_keywordedarguments(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

check_keywordedarguments(name="Sarah", age=24)
# name : Sarah
# age : 24

def check_keywordedarguments(**kwargs):
    return kwargs

print(check_keywordedarguments(fruit='apple', ordered=2))  # {'fruit': 'apple', 'ordered': 2}

# *args et **kwargs ensemble
def check_arguments_keywordedarguments(required_arg, *args, **kwargs):
    print(required_arg)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

check_arguments_keywordedarguments("argument requis")
check_arguments_keywordedarguments("argument requis", 1, 2, 'hey')
check_arguments_keywordedarguments("argument requis", 1, 2, 'hey', name="Sarah", age=24)

def check_arguments_keywordedarguments(*args, **kwargs):
    print('*args', args)
    print('**kwargs', kwargs)

check_arguments_keywordedarguments(10, 20, 30, name='John', surname='Doe')
# *args (10, 20, 30)
# **kwargs {'name': 'John', 'surname': 'Doe'}

# Attention à l'ordre des arguments :
# check_arguments_keywordedarguments(10, 20, 30, name='John', surname='Doe', 2)  # Erreur

# Utilisation de l'opérateur * et ** pour passer des arguments
def check(a, b, c):
    print(a, b, c)

a = [1, 2, 3]
check(*a)  # 1 2 3

a = {'a': 'Sarah', 'b': 24, 'c': 180}
check(**a)  # Sarah 24 180

# Conclusion :
# Les fonctions, *args et **kwargs permettent d'écrire du code flexible, réutilisable et puissant.
# Maîtriser ces concepts est essentiel pour développer des applications Python robustes.