human_years = int(input("Enter your animal's age in human years: "))
type_animal = input("Is your pet a cat or a dog? ")
Cats_years = 15 + (human_years - 1) * 9 if human_years > 1 else 15
Dogs_years = 15 + (human_years - 1) * 5 if human_years > 1 else 15

if type_animal.lower() == "cat":
    human_years == Cats_years
    print ("Your cat is " + str(Cats_years) + " years old in cat years.")
elif type_animal.lower() == "dog":
    human_years == Dogs_years
    print ("Your dog is " + str(Dogs_years) + " years old in dog years.")   