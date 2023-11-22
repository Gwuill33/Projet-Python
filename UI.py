import random
from dice import Dice
from character import Warrior, Mage, Thief, Character

from rich import print
from rich.console import Console
from rich.panel import Panel

console = Console()

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

        console.print("\n[bold]Bienvenue au combat des héros ![/bold]\n", justify="center" )

        class_options = [
            "1. Warrior: Big guy with big weapon.",
            "2. Mage: Spell caster.",
            "3. Thief: Sneaky bastard."
        ]

        console.print(Panel("\n".join(class_options), title="Character Classes", border_style="cyan", width=60))

        class_choice = input("Entrez la classe de votre choix (1, 2, ou 3): ")

        name = input("Quel est ton nom : ")
        if class_choice == '1':
            return Warrior(name, 20, 8, 3, Dice(6), 1)
        elif class_choice == '2':
            return Mage(name, 20, 8, 3, Dice(6), 0)
        elif class_choice == '3':
            return Thief(name, 20, 8, 3, Dice(6), 2)

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
            console.print(Panel(f"[bold purple]Round {round_number}[/bold purple]", width=11, border_style="blue"))
            self._char_list[0].attack(self._char_list[1])
            self._char_list[1].attack(self._char_list[0])

            self.display_character_info()

            round_number += 1

        console.print("[bold]Combat Finished![/bold]")
        if self._char_list[0].is_alive():
            console.print(f"[green]{self._char_list[0].get_name()} Wins![/green]")
        else:
            console.print(f"[green]{self._char_list[1].get_name()} Wins![/green]")

    def display_character_info(self):
        for character in self._char_list:
            console.print(Panel(f"{character}", title=f"{character.get_name()}", width=60, border_style="red"))

if __name__ == "__main__":
    combat = Combat()
    combat.start_combat()
