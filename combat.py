from __future__ import annotations
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
        warrior = Warrior("James", 20, 8, 3, Dice(6), 1, Items.random_items())
        mage = Mage("Elisa", 20, 8, 3, Dice(6), 0, Items.random_items())
        thief = Thief("Michel", 20, 8, 3, Dice(6), 2, Items.random_items())

        cars: list[Character] = [warrior, mage, thief]
        char1 = random.choice(cars)

        return char1
    
    def choose_character(self):
        char = input("""Choisi ton type de personnage entre :
1 - Warrior
2 - Mage 
3 - Thief 
""",)
        if char == '1' :
            name = input ("Quel est ton nom : ")
            item = input("""Choisi ton item entre :
1 - Epée
2 - Bouclier
3 - Potion(x2) 
""")
            char = Warrior(name, 20, 8, 3, Dice(6), 1, Items.choose_items(item))
            return char
        elif char == '2':
            name = input ("Quel est ton nom : ")
            item = input("""Choisi ton item entre :
1 - Epée
2 - Bouclier
3 - Potion(x2)
"""),
            char = Mage(name, 20, 8, 3, Dice(6), 0, Items.choose_items(item))
            return char
        elif char == '3':
            name = input ("Quel est ton nom : ")
            item = input("""Choisi ton item entre :
1 - Epée
2 - Bouclier
3 - Potion(x2)
""",)
            char = Thief(name, 20, 8, 3, Dice(6), 2, Items.choose_items(item))
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