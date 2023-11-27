from __future__ import annotations
print("\n")
from dice import Dice
from items import Items
import random

class Character:
    
    def __init__(self, name: str, max_hp: int, attack: int, defense: int, dice: Dice, initiative: int, items : Items):
        self._name = name
        self._max_hp = max_hp
        self._current_hp = max_hp
        self._attack_value = attack
        self._defense_value = defense
        self._dice = dice
        self._initiative = initiative
        self._items = items

    def __str__(self):
        return f"""{self._name} the Character enter the arena with :
    ■ attack: {self._attack_value} 
    ■ defense: {self._defense_value}"""
        
    def get_initiative(self):
        return self._initiative

    def get_defense_value(self):
        return self._defense_value
        
    def get_name(self):
        return self._name
        
    def is_alive(self):
        return self._current_hp > 0       

    def show_healthbar(self):
        missing_hp = self._max_hp - self._current_hp
        healthbar = f"[{"♥" * self._current_hp}{"♡" * missing_hp}] {self._current_hp}/{self._max_hp}hp"
        print(healthbar)

    def regenerate(self):
        self._current_hp = self._max_hp


    def increase_health(self):
        if self._items.get_name_items() == "Potion":
            print("🧪 Bonus: Potion in your face (+3 health)")
            self._current_hp += self._items.get_health_items()
        if self._current_hp > self._max_hp:
            self._current_hp = self._max_hp
        self.show_healthbar()

    def decrease_health(self, amount):
        self._current_hp -= amount
        if self._current_hp < 0:
            self._current_hp = 0
        self.show_healthbar()
        
    def compute_damages(self, roll, target):
        if self._items.get_name_items() == "Epée":
            print("🗡️ Bonus: Sword in your face (+3 attack)")
            return self._attack_value + roll + self._items.get_attack_items() + 3
        return self._attack_value + roll
        
    def attack(self, target: Character):
        if not self.is_alive():
            return
        roll = self._dice.roll()
        damages = self.compute_damages(roll, target)
        print(f"⚔️ {self._name} attack {target.get_name()} with {damages} damages (attack: {self._attack_value} + roll: {roll} + item: {self._items.get_name_items()})")
        target.defense(damages, self)
    
    def compute_defense(self, damages, roll, attacker):
        if self._items.get_name_items() == "Bouclier":
            print("🛡️ Bonus: Shield in your face (+3 defense)")
            return damages - self._defense_value - roll - self._items.get_defense_items()
        return damages - self._defense_value - roll
    
    def defense(self, damages, attacker: Character):
        roll = self._dice.roll()
        wounds = self.compute_defense(damages, roll, attacker)
        print(f"🛡️ {self._name} take {wounds} wounds from {attacker.get_name()} (damages: {damages} - defense: {self._defense_value} - roll: {roll})")
        self.decrease_health(wounds)

class Warrior(Character):
    def __init__(self):
        self.skills = {"critical attack": "critical attack"}

    def compute_damages(self, roll, target: Character):
        print("🪓 Bonus: Axe in your face (+3 attack)")
        return super().compute_damages(roll, target) + 3

    def critical_attack(self,roll, target: Character):
        return self.compute_damages(roll, target) * 2
    
    def attack(self, target: Character):
        if not self.is_alive():
            return
        roll = self._dice.roll()
        for i, (skill_name, skill_description) in enumerate(self.skills.items(), start=1):
            print(f"{i} - {skill_name}: {skill_description}")
        char = input
        if char > 1:
            damages = self.critical_attack(roll, target)
        print(f"⚔️ {self._name} attack {target.get_name()} with {damages} damages (attack: {self._attack_value} + roll: {roll})")
        target.defense(damages, self)

class Mage(Character):
    def __init__(self):
        self.skills = {"heal": "heal", "fireball": "fireball"}

    def compute_defense(self, damages, roll, attacker: Character):
        print("🧙 Bonus: Magic armor (-3 damages)")
        return super().compute_defense(damages, roll, attacker) - 3
    
    def fireball(self, target: Character):
        roll = random.int(3, 6)
        print("🔥 boule de feu dans ta gueule")     
        return self.compute_damages(roll, target)
    
    def soins(self):
        roll = random.int(4, 6)
        return self.increase_health(roll)
    
    def attack(self, target: Character):
        if not self.is_alive():
            return
        roll = self._dice.roll()
        for i, (skill_name, skill_description) in enumerate(self.skills.items(), start=1):
            print(f"{i} - {skill_name}: {skill_description}")
        char = input
        if char == 1:
            damages = self.fireball(target)
        elif char == 2:
            damages = self.soins()
        print(f"⚔️ {self._name} attack {target.get_name()} with {damages} damages (attack: {self._attack_value} + roll: {roll})")
        target.defense(damages, self)

class Thief(Character):
    def __init__(self):
        self.skills = {"Sneacky attack": "Sneacky attack", "critical attack": "critica attack"}

    def Sneacky_attack(self, roll, target: Character):
        return self.compute_damages(roll, target) + target.get_defense_value()
    
    def critical_attack(self,roll, target: Character):
        return self.compute_damages(roll, target) * 2
    
    def dodge(self):
        return super().compute_defense(0)
    
    def attack(self, target: Character):
        if not self.is_alive():
            return
        roll = self._dice.roll()
        for i, (skill_name, skill_description) in enumerate(self.skills.items(), start=1):
            print(f"{i} - {skill_name}: {skill_description}")
        char = input
        if char == 1:
            damages = self.Sneacky_attack(roll, target)
            target.defense(damages, self)
            
        elif char == 2:
            damages = self.critical_attack(roll, target)
            target.defense(damages, self)

    def defense(self, damages, attacker: Character):
        roll = self._dice.roll()
        wounds = self.compute_defense(damages, roll, attacker)
        print(f"🛡️ {self._name} take {wounds} wounds from {attacker.get_name()} (damages: {damages} - defense: {self._defense_value} - roll: {roll})")
        self.decrease_health(wounds)