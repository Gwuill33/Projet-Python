from __future__ import annotations
import random

class Items():
    
    def __init__(self, name_items, attack_items, defense_items, health_items, number_potion=0):
        self._name_items = name_items
        self._attack_items = attack_items
        self._defense_items = defense_items
        self._health_items = health_items
        self._number_potion = number_potion

    def __str__(self):
       pass
       
    def get_attack_items(self):
        return self._attack_items
    
    def get_defense_items(self):
        return self._defense_items
    
    def get_health_items(self):
        return self._health_items
    
    def get_name_items(self):
        return self._name_items
    
    def get_number_potion(self):
        return self._number_potion
    
    def set_number_potion(self, number_potion):
        self._number_potion = number_potion

    
    @staticmethod
    def choose_items() -> Items:
        item = input("""Choisi ton item entre :
1 - Epée
2 - Bouclier
3 - Potion (x2)
""",)
        if item == '1':
            return Epée()
        elif item == '2':
            return Bouclier()
        elif item == '3':
            return Potion()
        else:
            print("Choisi un item valide")
            return Items.choose_items()
        
    @staticmethod
    def random_items() -> Items:

        épée = Epée()
        bouclier = Bouclier()
        potion = Potion()
        items: list[Items] = [épée, bouclier, potion]
        item = random.choice(items)

        return item

class Epée(Items):
    def __init__(self):
        super().__init__("Epée", 3, 0, 0)

class Bouclier(Items):
    def __init__(self):
        super().__init__("Bouclier", 0, 4, 0)

class Potion(Items):
    def __init__(self):
        super().__init__("Potion", 0, 0, 5, 2)
        