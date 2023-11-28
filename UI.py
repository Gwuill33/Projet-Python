import random
from dice import Dice
from character import Warrior, Mage, Thief, Character
from items import Items


from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.progress import track
import time


console = Console()


for i in track(range(8), description="Processing..."):
    time.sleep(0.3)


class Items:
    
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
        

    def choose_items(self) -> Items:
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
            return self.choose_items()


class Combat:
    def __init__(self) -> None:
        self._char_list: list[Character] = []

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
        console.print("\n[bold]Bienvenue dans le combat des héros ![/bold]\n", justify="center")

        class_options = [
            "1. Warrior: Big guy with a big weapon.",
            "2. Mage: Spellcaster.",
            "3. Thief: Sneaky bastard."
        ]

        console.print(Align.center(Panel("\n".join(class_options), title="Character Classes", border_style="cyan", width=60)))

        class_choice = console.input(Align.center("Entrez la classe de votre choix (1, 2, ou 3): "))

        name = console.input(Align.center("Quel est ton nom : "))

        char = None
        if class_choice == '1':
            char = Warrior(name, 20, 8, 3, Dice(6), 1)
        elif class_choice == '2':
            char = Mage(name, 20, 8, 3, Dice(6), 0)
        elif class_choice == '3':
            char = Thief(name, 20, 8, 3, Dice(6), 2)
        else:
            console.print("Choix de classe invalide.")
            return self.choose_character()

        return char

    def combat_order(self):
        if self._char_list[1].get_initiative() > self._char_list[0].get_initiative():
            self._char_list[0], self._char_list[1] = self._char_list[1], self._char_list[0]
        elif self._char_list[1].get_initiative() == self._char_list[0].get_initiative():
            dice = random.choice([1, 2])
            if dice == 1:
                self._char_list[0], self._char_list[1] = self._char_list[1], self._char_list[0]

    def start_combat(self):
        self.create_combat()
        self.combat_order()
        round_number = 1

        while self._char_list[0].is_alive() and self._char_list[1].is_alive():
            console.print(Align.center(Panel(f"[bold purple]Round {round_number}[/bold purple]", width=11, border_style="blue")))
            self._char_list[0].attack(self._char_list[1])
            self._char_list[1].attack(self._char_list[0])

            self.display_character_info()

            round_number += 1
        
        console.print(Align.center("[bold]Combat Finished![/bold]"))
        if self._char_list[0].is_alive():
            console.print(Align.center(f"[green]{self._char_list[0].get_name()} Wins![/green]"))
        else:
            console.print(Align.center(f"[green]{self._char_list[1].get_name()} Wins![/green]"))


    def display_character_info(self):
        for character in self._char_list:
            console.print(Align.center(Panel(f"{character}", title=f"{character.get_name()}", width=60, border_style="red")))

if __name__ == "__main__":
    combat = Combat()
    combat.start_combat()