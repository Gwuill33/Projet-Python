from __future__ import annotations
import random
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()

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
        item = console.input(Align.center(Panel("""
[red]1 - Epée[/red]
[blue]2 - Bouclier[/blue]
[green]3 - Potion (x2)[/green]
""", border_style="Purple", title="Quel est ton item")))
        if item == '1':
            console.print(Align.center("[bold]Tu as choisi l'option 1 ![/bold]"))
            return Epée()
        elif item == '2':
            console.print(Align.center("[bold]Tu as choisi l'option 2 ![/bold]"))
            return Bouclier()
        elif item == '3':
            console.print(Align.center("[bold]Tu as choisi l'option 3 ![/bold]"))
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
        