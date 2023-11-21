from __future__ import annotations
from dice import Dice
from character import Character

class Items():
    
    def __init__(self, name_items, attack_items, defense_items, health_items):
        self._name_items = name_items
        self._attack_items = attack_items
        self._defense_items = defense_items
        self._health_items = health_items

    def __str__(self):
        return f"""{Character.get_name()} the Character enter the arena with : {self._name_items} with {self._attack_items} attack, {self._defense_items} defense and {self._health_items} health"""
    
    def get_name_items(self):
        return self._name_items
    
    def more_damage(self):
        return self._attack_items
    
    def minus_damage(self):
        return self._defense_items
    
    def more_health(self):
        return self._health_items
    
class Epée(Items):
        def __init__(self):
            super().__init__("Epée", 10, 0, 0)

class Bouclier(Items):
        def __init__(self):
            super().__init__("Bouclier", 0, 10, 0)

class Potion(Items):
        def __init__(self):
            super().__init__("Potion", 0, 0, 10) 