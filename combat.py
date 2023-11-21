import random

from dice import Dice
from character import Warrior, Mage, Thief, Character

print("\n")

class Combat:

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        pass

    def random_enemy(self):
        warrior = Warrior("James", 20, 8, 3, Dice(6))
        mage = Mage("Elisa", 20, 8, 3, Dice(6))
        thief = Thief("Michel", 20, 8, 3, Dice(6))

        cars: list[Character] = [warrior, mage, thief]
        char1 = random.choice(cars)

        return char1
    
    def choose_character(self):
        char = input("choisi ton charactère entre Warrior, Mage ou Thief",)
        if char == 'Warrior' :
            name = input ("quel est ton nom :")
            char = Warrior(name, 20, 8, 3, Dice(6), 1)
            return char
        elif char == 'Mage':
            name = input ("quel est ton nom :")
            char = Mage(name, 20, 8, 3, Dice(6), 0)
            return char
        elif char == 'Thief':
            name = input ("quel est ton nom :")
            char = Thief(name, 20, 8, 3, Dice(6), 2)
            return char
        

    def start_combat(self):
        char1 = self.random_enemy()
        char2 = self.choose_character()
        for _ in range(100):
            char1.regenerate()
            char2.regenerate()
        
        while char1.is_alive() and char2.is_alive():
            char1.attack(char2)
            char2.attack(char1)

if __name__ == "__main__":
    combat = Combat()
    combat.start_combat()