############################################################################################
#############################################I M P O R T S##################################
##############################################################################################
import random
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
menuPrompt=Prompt(choices=["1", "2", "3", "4"], show_choices=False)
menuPrompt.prompt_suffix = "✦"
menuPick= menuPrompt.ask("")
from rich.theme import Theme
console = Console()
with open("mobs.json") as m:
    mobs = json.load(m)


#############################
#T E X T   F U N C T I O N S#
#############################
def p(text, delay=0.25):
    """Normal text with a short pause after."""
    print(text)
    time.sleep(delay)


def pType(text):

    """Steady typewriter, flat and even."""

    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05)

    print()


def pCentered(text):
    """Print centered."""
    pRich(Align.center(text))



def pDialogue(text, style="cyan"):

    """Randomized typing intervals."""

    for char in text:
        console.print(char, style=style, end="")

        if char in ".!?":
            time.sleep(random.uniform(0.6, 1.1))      # Pause after sentence
        

        elif char in ",;:":
            time.sleep(random.uniform(0.25, 0.45))     # Pause after commas
        

        elif char == " " and random.random() < 0.05:
            time.sleep(random.uniform(0.2, 0.4))       # Random Pause after Word
        

        elif random.random() < 0.06:
            time.sleep(random.uniform(0.25, 0.6))      # Random Pause
        

        else:
            time.sleep(random.uniform(0.08, 0.15))     # normal keypress
        

    print()




def c():
    """Clear screen."""
    os.system('cls' if os.name == 'nt' else 'clear')






def menuInt(menuPick):

    """Keep asking until the player enters a number, then return it as an int."""

    while True:
        if menuPick.isdigit():
            return int(menuPick)
        else:
            p("Invalid Response")
            menuPick = input("> ")


# ---------- Game state ----------

stats = {
    "health": 20,
    "attack": 2,
    "shield": 5,
    "energy":20,
}

inventory = {}


# ---------- Text Scenes ----------

def intro():
    c()
    pDialogue("Day 2113")
    time.sleep(3)
    c()
    pDialogue("Preacher says the Lord is a shepherd.")
    time.sleep(1)
    c()
    pDialogue("I no longer believe myself to be among the kept.")
    time.sleep(2)
    c()
    pDialogue("There is a kind of dark that is not the absence of light, "
       "but the absence of anything that light would have shown.")
    time.sleep(2.7)
    c()
    pDialogue("My prayers are met with silence.")
    time.sleep(1)
    c()
    time.sleep(3)


# ---------- Loot ----------

lootTable = {
    "common": {
        "Healing": {"Cloth wrap": 2, "Bandage": 3},
        "Attack": {"Rusty Sword": 3, "Old Cleaver": 3},
    },
    "uncommon": {
        "Healing": {"Antibiotics": 5, "Small aid pack": 7},
        "Attack": {"Sharpened Iron": 4, "Switchblade": 5},
    },
    "rare": {
        "Healing": {"Medical Syringe": 12, "Military medkit": 15},
        "Attack": {"Longsword": 9, "Executioners Blade": 12},
    },
    "legendary": {
        # Instant Revive is an AMOUNT, not a heal value: if the player dies
        # while holding one, they continue at full HP.
        "Healing": {"Instant Revive": 1},
        "Attack": {"Zweihandler": 16},
    },
}


def discoverloot():
    roll = random.random()
    if roll < 0.05:
        tier = "legendary"
    elif roll < 0.15:
        tier = "rare"
    elif roll < 0.30:
        tier = "uncommon"
    else:
        tier = "common"

    droptier = random.choice(list(lootTable[tier]))
    lootedItem = random.choice(list(lootTable[tier][droptier]))

    if lootedItem in inventory:
        inventory[lootedItem] += 1
    else:
        inventory[lootedItem] = 1

    print(f"+1 {lootedItem} added to inventory.")


# ---------- Combat ----------

def playerAttack(mob):
    dmg = stats["attack"]
    if mob["shield"] > 0:
        if mob["shield"] > dmg:
            print(f"Monster has a shield! {dmg} damage deflected.")
        else:
            print("You broke the monster's shield!")
        mob["shield"] -= dmg
        if mob["shield"] < 0:
            mob["health"] -= abs(mob["shield"])
            mob["shield"] = 0
    else:
        mob["health"] -= dmg
    print(f"Monster has {mob['health']} remaining!")


def mobEncounter():
    mobName = random.choice(list(mobs.keys()))
    mob = mobs[mobName]
    p(mob["introPhrase"]["voice1"])
    time.sleep(1)
    p(f"You encountered a {mobName}!")
    while True:
        mobfightMenu(mobName, mob)
        break


def mobfightMenu(mobName, mob):
    pCentered(f"{mobName}\nHealth: {mob['health']}\nAttack: {mob['attack']}")
    print()
    print()
    pCentered("Select an Option:")
    pCentered("1) Fight\n2) Attempt to Flee\n3) View Inventory")
    menuPick = input("> ")


# ---------- Dice helpers ----------


def roll(num1=1, num2=6):
    return random.randint(num1, num2)

# ---------- Walking ----------


# ---------- Menus ----------



# ---------- Main ----------

# intro()
# print(pyfiglet.figlet_format("WEST OF MERCY", font="doom"))
# time.sleep(4)

# pr("Good evening, traveler.")
# time.sleep(2)
# c()
#TODO - Make this menu look nicer, put it into a function
# p("Select an option")
# p("1] Head West")
# p("2] Exit Game")
# menuPick = input("> ")
##TODO - Clean this up
# if menuPick == "1":
#     while True:
#         choice = show_menu()
#         if choice == "1":
#             walk()
#         elif choice == "2":
#             stats["energy"] += 1
#             p("You rest a while. (+1 Energy)")
#         elif choice == "3":
#             print(inventory)
#         elif menuPick == "2":
#             break

stats_line=Text()
stats_line.append("♥|", style="bold red")
stats_line.append(f"{stats['health']}", style="red bold")
stats_line.append("    ✦ |", style="yellow")
stats_line.append(f"{stats['energy']}", style="bold yellow")
stats_line.append("")
console.print(Panel(stats_line, title="Stats", expand=False,))



# moveMenu=Table(box=None)
# moveMenu.add_column(highlight=True, header="Select an Option", header_style="bold cyan" )
# moveMenu.add_row("[dim]1)[/dim] Move West")
# moveMenu.add_row("[dim]2)[/dim] Rest")
# moveMenu.add_row("[dim]3)[/dim] Inventory")
# moveMenu.add_row("[dim]4)[/dim] Exit")
# console.print(moveMenu)
# menuPick=Prompt.ask("", choices=["1", "2", "3", "4"], show_choices=False, prompt_suffix="✦")

# console.print(20)
# console = Console()
# text = Text("Hello, World!")
# text.stylize("bold magenta", 0, 6)
# console.print(text)


def loadingscreen():
    c()
    for n in range(6):
        print("●"*n + "○"*(5-n),end="", flush=True)
        time.sleep(1)
        c()



#Helpful Unicodes
# ⚠
# ☢︎
# ⴵ
# 🜲
# ╰── ──╮
# ⃟


