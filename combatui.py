from __future__ import annotations
import random
from dice import Dice
from character import Warrior, Mage, Thief, Character
from items import Items
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.progress import track
import time


print("\n")

console = Console()

for i in track(range(8), description="Processing..."):
    time.sleep(0.3)

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
        char = console.input(Align.center(Panel("""
[red]1 - Warrior : Fort mais stupide[/red]
[blue]2 - Mage : Intelligent mais faible[/blue]
[yellow]3 - Thief : Discret comme un rat[/yellow]
""",border_style="cyan", title="Choisis ta classe")))
        # Le choix du personnage est le Warrior
        if char == '1' :
            console.print(Align.center("[bold]Tu as choisi l'option 1 ![/bold]"))
            name = console.input (Align.center("[green bold]Quel est ton nom : [/green bold]"))
            console.print(Align.center(f"[blue bold]Tu as choisis ton nom ! Ça sera {name}[/blue bold]"))
            char = Warrior(name, 20, 8, 3, Dice(6), 1, Items.choose_items())
            return char
        # Le choix du personnage est le Mage
        elif char == '2':
            console.print(Align.center("[bold]Tu as chosi l'option 2 ![/bold]"))
            name = console.input (Align.center("[green bold]Quel est ton nom : [/green bold]"))
            char = Mage(name, 20, 8, 3, Dice(6), 0, Items.choose_items())
            return char
        # Le choix du personnage est le Thief
        elif char == '3':
            console.print(Align.center("[bold]Tu as choisis l'option 3 ![/bold]"))
            name = console.input (Align.center("[green bold]Quel est ton nom : [/green bold]"))
            char = Thief(name, 20, 8, 3, Dice(6), 2, Items.choose_items())
            return char
        # Si le choix n'est pas valide
        else:
            console.print("[red]Choisis un personnage valide[/red]")
            return self.choose_character()
        


    def choose_actions(self):

        actions = console.input(Align.center(Panel(f"""
[red]1 - Attack[/red]
[blue]2 - Afficher barre de vie[/blue]
[green]3 - Potion (Nombre de potions : {self._char_list[0]._items.get_number_potion()})[/green]
""",border_style="red", title="Quelle est ton action")))
        if actions == '1' :
            console.print(Align.center("[bold]Tu as choisi l'option 1 ![/bold]"))
            time.sleep(0.2)
            return self._char_list[0].attack(self._char_list[1])
        elif actions == '2':
            console.print(Align.center("[bold]Tu as choisi l'option 2 ![/bold]"))
            time.sleep(0.2)
            print(self._char_list[0].show_healthbar())
            return self.choose_actions()
        elif actions == '3' and self._char_list[0]._items.get_number_potion() > 0:
            console.print(Align.center("[bold]Tu as choisi l'option 3 ![/bold]"))
            time.sleep(0.2)
            self._char_list[0]._items.set_number_potion(self._char_list[0]._items.get_number_potion() - 1)
            return self._char_list[0].increase_health()
        else:
            print("[red]Choisis une action valide[/red]")
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