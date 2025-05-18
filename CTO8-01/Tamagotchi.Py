# Tamagotchi Game
# Stats for the Tamagotchi:
# 100/100 = happy, full of enery , hungry
# 0/100 = sad, not hungry, tired
# increase/decrease the stats by a random amount

import random
import time

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.age = 0

    def status(self):
        hungry = ["Very Full", "Full", "Normal", "Hungry", "Very Hungry", "Hangry!"][self.hunger // 25]
        tired = ["Exhausted!", "Very Tired", "Tired", "Normal", "Energetic", "Extremely Energetic!"][self.energy // 25]
        angry = ["Angry!", "Very Bored", "Bored", "Normal", "Happy", "Extremely Happy!"][self.happiness // 25]

        print(f"\n{self.name}'s status:")
        print(f"Age: {self.age}")
        print(f"Hunger: {self.hunger}/100 - {hungry}")
        print(f"Happiness: {self.happiness}/100 - {angry}")
        print(f"Energy: {self.energy}/100 - {tired}\n")

    def feed(self):
        choice = random.choice(["1", "2", "3", "4"])
        
        if choice == "1":
            self.hunger = max(self.hunger - random.randint(5, 10), 0)
            self.happiness = min(self.happiness + random.randint(5, 15), 100)
            print(f"{self.name} enjoyed a snack!")
        elif choice == "2":
            self.hunger = max(self.hunger - random.randint(15, 25), 0)
            print(f"{self.name} had a meal!")
        elif choice == "3":
            self.hunger = max(self.hunger - random.randint(25, 40), 0)
            self.energy = max(self.energy - random.randint(5, 10), 0)
            print(f"{self.name} had a feast!")
        elif choice == "4":
            self.happiness = min(self.happiness + random.randint(10, 20), 100)
            self.hunger = max(self.hunger - random.randint(2, 5), 0)
            print(f"{self.name} enjoyed a treat!")


    def play(self):
        print(f"Playing with {self.name}...")
        mini_game_result = mini_game()
        self.happiness = min(self.happiness + mini_game_result, 100)
        self.energy = max(self.energy - random.randint(9, 15), 0)
        self.hunger = min(self.hunger + random.randint(4, 9), 100)

    def sleep(self):
        print(f"{self.name} is sleeping...")
        self.energy = min(self.energy + random.randint(16, 23), 100)
        self.happiness = max(self.happiness - random.randint(3, 9), 0)
        self.hunger = min(self.hunger + random.randint(10, 17), 100)

    def age_up(self):
        self.age += 1
        self.hunger = min(self.hunger + random.randint(1, 5), 100)
        self.happiness = max(self.happiness - random.randint(1, 5), 0)
        self.energy = max(self.energy - random.randint(1, 5), 0)
        print(f"\n{self.name} has grown up!\n")

def mini_game():
    """ Randomly selects a mini-game and returns the skill boost. """
    games = [bubble_pop, memory_match, speed_dash, push_up_challenge, tama_talk, dress_up, dance_party]
    game = random.choice(games)
    return game()

def bubble_pop():
    correct_bubble = random.randint(1, 5)
    start_time = time.time()
    choice = int(input("\nBubble Pop! Choose a bubble (1-5): "))
    end_time = time.time()
    
    if choice == correct_bubble and (end_time - start_time) < 3:
        print("Success! Your Tamagotchi's reflexes improved.")
        return 10
    else:
        print("Oops! You missed.")
        return -5

def memory_match():
    print("\nMemory Match! Try to remember the sequence.")
    sequence = [random.randint(1, 4) for _ in range(3)]
    print("Sequence:", sequence)
    time.sleep(2)
    print("\nNow, enter the sequence:")
    guess = [int(input(f"Number {i+1}: ")) for i in range(3)]
    
    if guess == sequence:
        print("Correct! Intelligence increased.")
        return 10
    else:
        print("Wrong! Intelligence slightly decreased.")
        return -5

def speed_dash():
    print("\nQuick Snack Dash! Press Enter as fast as possible!")
    input("Ready? Press Enter now!")
    reaction_time = time.time() - time.time()  # Measures response speed

    if reaction_time < 2:
        print("Fast reflexes! Speed increased.")
        return 10
    else:
        print("Too slow!")
        return -5
    
def push_up_challenge():
    print("\nPush-Up Challenge! Tap Enter 5 times fast!")
    taps = 0
    
    while taps < 5:
        input("Tap! (Press Enter)")
        taps += 1
    
    print("Strength boosted!")
    return 10

def tama_talk():
    print("\nTama Talk! Choose the best response.")
    choice = input("Your Tama asks, 'Do you like me?' (Yes/No): ").lower()
    
    if choice == "yes":
        print("Friendship strengthened!")
        return 10
    else:
        print("Your Tama is sad!")
        return -5
    
def dress_up():
    print("\nDress-Up Time! Pick a cool outfit.")
    outfit = input("Choose between Fancy, Casual, or Sporty: ").lower()

    print(f"{outfit.title()} outfit selected!")
    return 10

def dance_party():
    print("\nDance Party! Follow the beat (Type 'Dance' 3 times).")
    for i in range(3):
        choice = input(f"Step {i+1}: ").lower()
        if choice != "dance":
            print("Oops! Missed a beat.")
            return -5
    
    print("Perfect dance! Happiness increased.")
    return 10

def menu():
    print("\n1. Play")
    print("2. Sleep")
    print("3. Feed")
    print("4. Exit")

def playwpet():
    print("\n####### Tamagotchi Game #######")
    pet = Tamagotchi(input("\nEnter your pet's name: "))
    
    while True:
        time.sleep(1.5)
        pet.status()
        menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            pet.play()
            pet.age_up()
        elif choice == "2":
            pet.sleep()
            pet.age_up()
        elif choice == "3":
            pet.feed()
            pet.age_up()
        elif choice == "4":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Try again.")

playwpet()
