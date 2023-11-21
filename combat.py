import random

from dice import Dice
from character import Warrior, Mage, Thief, Character
from items import Items

print("\n")

class Combat:

    def __init__(self) -> None:
        self._char_list: list[Character] = []

    def __str__(self) -> str:
        pass

    def create_combat(self):
        self._char_list = [self.choose_character(), self.random_enemy()]

    def random_enemy(self):
        warrior = Warrior("James", 20, 8, 3, Dice(6), 1)
        mage = Mage("Elisa", 20, 8, 3, Dice(6), 0)
        thief = Thief("Michel", 20, 8, 3, Dice(6), 2)

        cars: list[Character] = [warrior, mage, thief]
        char1 = random.choice(cars)

        return char1
    
    def choose_character(self):
        char = input("Choisi ton charactère entre Warrior, Mage ou Thief : ",)
        if char == 'Warrior' :
            name = input ("Quel est ton nom : ")
            char = Warrior(name, 20, 8, 3, Dice(6), 1)
            return char
        elif char == 'Mage':
            name = input ("Quel est ton nom : ")
            char = Mage(name, 20, 8, 3, Dice(6), 0)
            return char
        elif char == 'Thief':
            name = input ("Quel est ton nom : ")
            char = Thief(name, 20, 8, 3, Dice(6), 2)
            return char
        
    def combat_order(self):
        if (self._char_list[1].get_initiative() > self._char_list[0].get_initiative()):
            self._char_list[0], self._char_list[1] = self._char_list[1], self._char_list[0]
        if (self._char_list[1].get_initiative() == self._char_list[0].get_initiative()):
            dice = random.choice([1, 2])
            if dice == 1 : self._char_list[0], self._char_list[1] = self._char_list[1], self._char_list[0]

    def start_combat(self):
        self.create_combat()
        self.combat_order()
        while self._char_list[0].is_alive() and self._char_list[1].is_alive():
                self._char_list[0].attack(self._char_list[1])
                self._char_list[1].attack(self._char_list[0])
      
if __name__ == "__main__":
    combat = Combat()
    combat.start_combat()