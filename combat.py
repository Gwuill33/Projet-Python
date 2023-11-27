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
        # Le choix du personnage est le Warrior
        if char == '1' :
            name = input ("Quel est ton nom : ")
            char = Warrior(name, 20, 8, 3, Dice(6), 1, Items.choose_items())
            return char
        # Le choix du personnage est le Mage
        elif char == '2':
            name = input ("Quel est ton nom : ")
            char = Mage(name, 20, 8, 3, Dice(6), 0, Items.choose_items())
            return char
        # Le choix du personnage est le Thief
        elif char == '3':
            name = input ("Quel est ton nom : ")
            char = Thief(name, 20, 8, 3, Dice(6), 2, Items.choose_items())
            return char
        # Si le choix n'est pas valide
        else:
            print("Choisissez un personnage valide")
            return self.choose_character()


    def choose_actions(self):

        actions = input(f"""Choisi ton action entre :
1 - Attack
2 - Defense
3 - Potion (Nombre de potions : {self._char_list[0]._items.get_number_potion()})
""",)
        if actions == '1' :
            return self._char_list[0].attack(self._char_list[1])
        elif actions == '2':
            return self._char_list[0].defense(self._char_list[1])
        elif actions == '3' and self._char_list[0]._items.get_number_potion() > 0:
            self._char_list[0]._items.set_number_potion(self._char_list[0]._items.get_number_potion() - 1)
            return self._char_list[0].increase_health()
        else:
            print("Choisi une action valide")
            return self.choose_actions()

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
                self.choose_actions()
                self._char_list[1].attack(self._char_list[0])
      
if __name__ == "__main__":
    combat = Combat()
    combat.start_combat()