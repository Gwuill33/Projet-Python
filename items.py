from __future__ import annotations
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

    def choose_items(self):
        item = input("Choisi ton item entre Epée, Bouclier ou Potion(x2) : ",)
        if item == 'Epée' :
            return Items("Epée", 3, 0, 0)
        elif item == 'Bouclier':
            return Items("Bouclier", 0, 3, 0)
        elif item == 'Potion':
            return Items("Potion", 0, 0, 5)
        