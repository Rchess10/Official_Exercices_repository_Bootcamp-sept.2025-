# # ----------------------------------------
# # Introduction to OOP (Object Oriented Programming)
# # ----------------------------------------

# # Table of Contents
# # - Introduction
# # - What you will learn
# # - Object Oriented Programming
# # - Abstract
# # I. Classes
# # II. Objects (instances)
# # III. Defining a class
# # IV. Creating an object (instance)
# # V. Attributes
# # VI. The __init__ method
# # - Exercise

# # Last Updated: August 7th, 2024

# # --- Introduction ---
# # Python is an object-oriented programming language.
# # Almost everything in Python is an object with its properties and methods.
# # A Class is like a blueprint for creating objects.

# # --- What you will learn ---
# # - Classes and Objects
# # - self parameter
# # - __init__() method

# # --- Object Oriented Programming ---
# # OOP means structuring programs so that properties and behaviors are bundled into individual objects.
# # Example: An object could represent a person with a name, age, address, etc., and behaviors like walking, talking, breathing.

# # --- I. Classes ---
# # A class is a blueprint for how something should be defined.
# # It provides structure but not actual content.
# # Example: Tracking animals with a class Animal.

# # --- II. Objects (instances) ---
# # An instance is a copy of the class with actual values.
# # Example: A dog named Roger, eight years old, is an instance of the Dog class.

# # --- III. Defining a class ---
# class Dog():
#     pass  # 'pass' is a placeholder, the class is empty for now

# # --- IV. Creating an object (instance) ---
# shelter_dog = Dog()  # Creates an object of the class Dog


# # --- V. Attributes ---
# # Objects have attributes (variables that belong to the object)
# shelter_dog.color = "Brown"  # Assigns a color attribute to shelter_dog

# # --- VI. The __init__ method ---
# class Dog():
#     # Initializer / Instance Attributes
#     def __init__(self, name_of_the_dog):
#         print("A new dog has been initialized!")
#         print("His name is", name_of_the_dog)
#         self.name = name_of_the_dog

# shelter_dog = Dog('Rex')
# other_shelter_dog = Dog("Jimmy")

# # --- Example: Person class ---
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# first_person = Person("John", 36)
# print(first_person.name)  # John
# print(first_person.age)   # 36

# --- Exercise ---
# Analyse the code below. What will be the output?
# Explain the goal of the __init__() method

# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# ## create an instance of the class
# p = Point(3, 4)

# ## access the attributes
# print("p.x is:", p.x)  # p.x is: 3
# print("p.y is:", p.y)  # p.y is: 4

# The __init__() method initializes the attributes of the object when it is created.

###### exemple fait en cours

# class Robot():
#     def __init__(self, name, color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight

# robot = Robot("Igor", "Blue", "180kg") 
             
# p = (f'{robot.name} is a {robot.color} robot and weight over {robot.weight}')
# print(p)

# class person():
#     def __init__(self, name, age): 
#         self.name = name 
#         self.age = age 
#     def show_details(self):
#         print(f'Hello, my name is {self.name}')

# first_person = person("Jhon","65")
# first_person.show_details()

# class BankAccount:
     
#      def __init__(self, account_number, balance=0):
#          self.account_number = account_number
#          self.balance = balance
#          self.transactions = []

#      def view_balance(self):
#          self.transactions.append("View Balance")
#          print(f"Balance for account {self.account_number}: {self.balance}")

#      def deposit(self, amount):
#          if amount <= 0:
#             print("Invalid amount")
#          elif amount < 100:
#             print("Minimum deposit is 100")
#          else:
#             self.balance += amount
#             self.transactions.append(f"Deposit: {amount}")
#             print("Deposit Succcessful")

#      def withdraw(self, amount):
#          if amount > self.balance:
#             print("Insufficient Funds")
#          else:
#             self.balance -= amount
#             self.transactions.append(f"Withdraw: {amount}")
#             print("Withdraw Approved")
#             return amount

#      def view_transactions(self):
#          print("Transactions:")
#          print("-------------")
#          for transaction in self.transactions:
#             print(transaction)

# account = BankAccount(account_number="123456", balance=500)
# # Afficher le solde
# account.view_balance()  # Affiche le solde et ajoute "View Balance" dans l'historique

# # Faire un dépôt
# account.deposit(200)    # Ajoute 200 au solde et enregistre la transaction

# # Faire un retrait
# account.withdraw(100)   # Retire 100 du solde et enregistre la transaction

# # Afficher l'historique des transactions
# account.view_transactions()


