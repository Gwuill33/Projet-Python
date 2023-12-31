from __future__ import annotations
print("\n")
from dice import Dice
from items import Items
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()

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
        healthbar = f"[red][{'♥' * self._current_hp}{'♡' * missing_hp}] {self._current_hp}/{self._max_hp}hp[/red]"
        console.print(Align.center(Panel((healthbar), border_style="red",width=50)))

    def regenerate(self):
        self._current_hp = self._max_hp


    def increase_health(self):
        if self._items.get_name_items() == "Potion":
            console.print(Align.center("[green]🧪 Bonus: Potion in your face (+3 health)[/green]"))
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
            console.print(Align.center("[red]🗡️ Bonus: Sword in your face (+3 attack)[/red]"))
            return self._attack_value + roll + self._items.get_attack_items() + 3
        return self._attack_value + roll
        
    def attack(self, target: Character):
        if not self.is_alive():
            return
        roll = self._dice.roll()
        damages = self.compute_damages(roll, target)
        console.print(Align.center(f"⚔️ {self._name} attack {target.get_name()} with {damages} damages (attack: {self._attack_value} + roll: {roll} + item: {self._items.get_name_items()})"))
        target.defense(damages, self)
    
    def compute_defense(self, damages, roll, attacker):
        if self._items.get_name_items() == "Bouclier":
            console.print(Align.center("[blue]🛡️ Bonus: Shield in your face (+3 defense)[/blue]"))
            return damages - self._defense_value - roll - self._items.get_defense_items()
        return damages - self._defense_value - roll
    
    def defense(self, damages, attacker: Character):
        roll = self._dice.roll()
        wounds = self.compute_defense(damages, roll, attacker)
        console.print(Align.center(f"🛡️ {self._name} take {wounds} wounds from {attacker.get_name()} (damages: {damages} - defense: {self._defense_value} - roll: {roll})"))
        self.decrease_health(wounds)

class Warrior(Character):
    def compute_damages(self, roll, target: Character):
        console.print(Align.center("🪓 Bonus: Axe in your face (+3 attack)"))
        return super().compute_damages(roll, target) + 3

class Mage(Character):
    def compute_defense(self, damages, roll, attacker: Character):
        console.print(Align.center("🧙 Bonus: Magic armor (-3 damages)"))
        return super().compute_defense(damages, roll, attacker) + 3

class Thief(Character):
    def compute_damages(self, roll, target: Character):
        console.print(Align.center(f"🔪 Bonus: Sneacky attack (+{target.get_defense_value()} damages)"))
        return super().compute_damages(roll, target) + target.get_defense_value()


if __name__ == "__main__":
    character1 = Warrior("Salim", 20, 8, 3, Dice(6))
    character2 = Thief("Lisa", 20, 8, 3, Dice(6))
    print(character1)
    print(character2)
    
    while (character1.is_alive() and character2.is_alive()):
        character1.attack(character2)
        character2.attack(character1)