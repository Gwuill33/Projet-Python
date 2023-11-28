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
            char = Warrior(name, 20, 8, 3, Dice(6), 1, self.choose_items())
        elif class_choice == '2':
            char = Mage(name, 20, 8, 3, Dice(6), 0, self.choose_items())
        elif class_choice == '3':
            char = Thief(name, 20, 8, 3, Dice(6), 2, self.choose_items())
        else:
            console.print("Choix de classe invalide.")
            return self.choose_character()

        return char

    def choose_items(self):
        console.print("[bold]Choisissez vos items :[/bold]")
        items = Items.choose_items()
        self.display_items_info(items)
        return items

    def display_items_info(self, items):
        console.print(Panel(f"Items choisis : {items.get_name_items()}", title="Items Info", border_style="green", width=60))

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