class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animal = {}

    def animal_add(self, animal_type, count = 1):
             if animal_type in self.animal:
                self.animal[animal_type] += count
             else: 
                self.animal[animal_type] = count

    def get_info(self):
        info = f"{self.name}'s farm\n"
        for animal, count in self.animal.items():
            info += f"{animal:<10}: {count}\n"
        info += "E-I-E-I-0!"
        return info
    def get_animal_types(self):
        return sorted(self.animal.keys())

    def get_short_info(self):
        animal_list = []
        for animal, count in self.animal.items():
            name = animal + "s" if count > 1 else animal
            animal_list.append(name)
        animals_str = ", ".join(animal_list[:-1])
        if animal_list:
            if len(animal_list) > 1:
                animals_str += f" and {animal_list[-1]}"
            else:
                animals_str = animal_list[0]
        return f"{self.name}'s farm has {animals_str}."

laferme = Farm("Ma ferme")
laferme.animal_add("cow")
laferme.animal_add("pig", 3)
laferme.animal_add("horse", 2)
laferme.animal_add("pig", 2)
laferme.animal_add("cow", 4)

print(laferme.get_info())
print(laferme.animal)








