class ZooAnimal:
    def __init__(self, name, species,food):
        self.name = name
        self.species = species
        self.food= food

    def describe(self):
        return f"{self.name} is a {self.species}."
    def hungry(self):
        return f"{self.name} is hungry and wants to eat {self.food}."
lion= ZooAnimal("Leo", "Lion","Deer")
tiger= ZooAnimal("Tig", "Tiger","Deer")
print(lion.describe())
print(lion.hungry())