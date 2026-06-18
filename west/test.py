import random
from dialogues import lootencounters, buildingencounters, tavernencounters
import time
import os
import json
import pyfiglet
from rich import print as pRich, box
from rich.panel import Panel
from rich.align import Align
from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich.prompt import Prompt
from rich.theme import Theme
console = Console()
with open("statss.json") as m:

    mobs = json.load(m)
stats = {
    "health": 20,
    "attack": 2,
    "shield": 5,
    "energy": 20,
}

def player_stats():
    stats_line = Text()
    stats_line.append("♥|", style="bold red")
    stats_line.append(f"{stats['health']}", style="red bold")
    stats_line.append("    ✦ |", style="yellow")
    stats_line.append(f"{stats['energy']}", style="bold yellow")
    stats_line.append("")
    console.print(Panel(stats_line, title="Stats", expand=False,))
 
def c():
    """Clear screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
 
def playerAttack(mob,mobName):
    number=random.random()


    print("Charging Attack...")
    time.sleep(5)


    dmg = stats["attack"]


    if number < 0.9:

        if mob["shield"] > 0:


            if mob["shield"] > dmg:
                print(f"{mobName} has a shield! {dmg} damage deflected.")
            else:
                print(f"You broke{mobName}'s shield!")
                mob["shield"] -= dmg


            if mob["shield"] < 0:
                mob["health"] -= abs(mob["shield"])
                mob["shield"] = 0


        else:
            mob["health"] -= dmg
            if mob["health"]<=0:
                print(f"{mobName} killed!")
                time.sleep(5)
                return
            

        print(f"{mobName} has {mob['health']} health remaining!")
        time.sleep(5)
        return

    else:
        print("Attack missed!")
        return


def menu_move_rest_inv_exit():
    playMenu = Table(box=None)
    playMenu.add_column(header="Select an Option", header_style="bold red")
    playMenu.add_row("[dim][cyan]1[/cyan])[/dim] [white]Move West[/white]" " [dim](-1 [yellow]✦[/yellow][/dim]")
    playMenu.add_row("[dim][cyan]2[/cyan])[/dim] [white]Rest[/white]" " [dim](+1 [yellow]✦[/yellow])[/dim]")
    playMenu.add_row("[dim][cyan]3[/cyan])[/dim] Inventory")
    playMenu.add_row("[dim][cyan]4[cyan])[/dim] Exit")
    console.print(playMenu)

def mobEncounter():
    mobName = random.choice(list(mobs.keys()))
    mob = mobs[mobName]
    print(mob["introPhrase"]["voice1"])
    time.sleep(3)
    print(f"You encountered {mobName}!")
    c()
    while stats["health"] > 0 and mob["health"] > 0:
        mobstats=Text()
        mobstats.append("♥|", style="bold red")
        mobstats.append(f"{mob['health']}", style="red bold")
        mobstats.append("    ⚔  |", style="blue")
        mobstats.append(f"{stats['attack']}", style="bold blue")
        console.print(Panel(mobstats, title=mobName, expand=False))
        time.sleep(5)
        player_stats()

        print("Select an Option:")
        print("1) Fight\n2) Attempt to Flee\n3) View Inventory")
        menuPick = input("> ")
        time.sleep(3)
        if menuPick == "1":
            playerAttack(mob, mobName)
        elif menuPick == "2":
            time.sleep(1)
            print("Attempting to flee.")
            risk = random.random()
            if risk < 0.5:
                time.sleep(5)
                stats['energy'] -= 1
                console.print("[red]Escape Failed.[/red]")
                console.print("[red]-1 ✦[/red]")
                
            else:
                time.sleep(5)
                print("Successfully fled.")
                return


#while True:
    player_stats()
    menu_move_rest_inv_exit()
    u=input(">")
    if u =="1":
        stats["energy"]-=1
        mobEncounter()


def mobAttack(mob, mobName)
    
    number=random.random()


    pType(f"{mobName} is preparing attack...")
    time.sleep(3)


    dmg = stats["attack"]
    crit=random.randrange(1,11)
    if crit in ["9", "10"]:
        dmg = dmg * 2
        pType("Critical hit!")


    if number < 0.9:

        if stats["shield"] > 0:


            if stats["shield"] > dmg:
                pType(f"Your shield protected you! {dmg} damage deflected.")
            else:
                pType(f"Your shield is broken!")
                stats["shield"] -= dmg


            if stats["shield"] < 0:
                stats["health"] -= abs(stats["shield"])
                stats["shield"] = 0


        else:
            stats["health"] -= dmg
            if stats["health"]<=0:
                c()
                pDialogue("The winter grows colder.")
                time.sleep(2)
                pDialogue("You've found yourself just west of mercy.")
                time.sleep(2)
                c()
                pType("Game Over. No Health Remaining")
                return
            
        return

    else:
        pType("Attack missed!")
        return