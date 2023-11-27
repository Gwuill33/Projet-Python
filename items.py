from __future__ import annotations
from dice import Dice
import random
# from character import Character

class Items():
    
    def __init__(self, name_items, attack_items, defense_items, health_items):
        self._name_items = name_items
        self._attack_items = attack_items
        self._defense_items = defense_items
        self._health_items = health_items

    def __str__(self):
       pass
       
    def get_name_items(self):
        return self._name_items
    
    def more_damage(self):
        return self._attack_items
    
    def minus_damage(self):
        return self._defense_items
    
    def more_health(self):
        return self._health_items
    

    def choose_items(item: str) -> Items:
        if item == '1' :
            return Epée()
        elif item == '2':
            return Bouclier()
        elif item == '3':
            return Potion()
        
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
        super().__init__("Bouclier", 0, 3, 0)

class Potion(Items):
    def __init__(self):
        super().__init__("Potion", 0, 0, 5)


        