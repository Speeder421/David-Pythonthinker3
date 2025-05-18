# Tamagotchi Game
# Stats for the Tamagotchi:
# 100/100 = happy, full of enery , hungry
# 0/100 = sad, not hungry, tired
# increase/decrease the stats by a random amount


import random,time

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.age = 0

    def status(self):
        hungry=""
        tired=""
        angry=""
        if self.hunger == 100:
            hungry="Hangry!"
        elif self.hunger >= 75:
            hungry="Very Hungry"
        elif self.hunger >= 51:
            hungry="Hungry"
        elif self.hunger == 50:
            hungry="Normal"
        elif self.hunger >= 26:
            hungry="Full"
        elif self.hunger >= 0:
            hungry="Very Full"

        if self.energy == 100:
            tired="Extremely Energetic!"
        elif self.energy >= 75:
            tired="Very Energetic"
        elif self.energy >= 51:
            tired="Energetic"
        elif self.energy == 50:
            tired="Normal"
        elif self.energy >= 26:
            tired="Tired"
        elif self.energy >= 1:
            tired="Very Tired"
        elif self.energy == 0:
            tired="Exhausted!"

        if self.happiness == 100:
            angry="Extremely Happy!"
        elif self.happiness >= 75:
            angry="Very Happy"
        elif self.happiness >= 51:
            angry="Happy"
        elif self.happiness == 50:
            angry="Normal"
        elif self.happiness >= 26:
            angry="Bored"
        elif self.happiness >= 1:
            angry="Very Bored"
        elif self.happiness == 0:
            angry="Angry!"

        print(f"{self.name}'s status:")
        print(f"Age: {self.age}")
        print(f"Hunger: {self.hunger}/100 - {hungry}")
        print(f"Happiness: {self.happiness}/100 - {angry}")
        print(f"Energy: {self.energy}/100 - {tired}")
    def feed(self):
        self.hunger = max(self.hunger-random.randint(10,20),0)
        self.happiness = max(self.happiness-random.randint(2,7),0)
        self.energy = min(self.energy+random.randint(9,15),100)
        print(f"{self.name} is fed a meal!")
    def play(self):
        self.happiness = min(self.happiness+random.randint(13,20),100)
        self.energy = max(self.energy-random.randint(9,15),0)
        self.hunger = min(self.hunger+random.randint(4,9),100)
        print(f"{self.name} played a game!")
    def sleep(self):
        self.energy = min(self.energy+random.randint(16,23),100)
        self.happiness = max(self.happiness-random.randint(3,9),0)
        self.hunger = min(self.hunger+random.randint(10,17),100)
        print(f"{self.name} slept!")
    def age_up(self):
        self.age += 1
        self.hunger = min(self.hunger+random.randint(1,5),100)
        self.happiness = max(self.happiness-random.randint(1,5),0)
        self.energy = max(self.energy-random.randint(1,5),0)
        print(f"{self.name} has grown up!")

def menu():
    print("1. Play")
    print("2. Sleep")
    print("3. Feed")
    print("4. Exit")

def playwpet():
    print("#######Tamagotchi Game#######")
    pet=Tamagotchi(input("Enter your pet's name: "))
    while True:
        time.sleep(1.5)
        pet.status()
        menu()
        choice = input("Choose an option: ")
        if choice == "1":
            print(f"Playing with {pet.name}...")
            pet.play()
            pet.age_up()
        elif choice == "2":
            print(f"{pet.name} is sleeping...")
            pet.sleep()
            pet.age_up()
        elif choice == "3":
            print(f"Feeding {pet.name}...")
            pet.feed()
            pet.age_up()
        elif choice == "4":
            print("Thank you for playing!")
            print("Closing the game...")
            break
        else:
            print("Invalid choice. Please try again.")
playwpet()