############################################################################################
#############################################I M P O R T S##################################
##############################################################################################
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
 
def ask(valid):
    while True:
        choice = input("✦ ")
        if choice in valid:
            return choice
        p("Invalid choice.")
 
 
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
 
def titlescreen():
    print(pyfiglet.figlet_format("WEST OF MERCY", font="doom"))
    time.sleep(4)
 
 
def loadingscreen():
    c()
    for n in range(6):
        print("●"*n + "○"*(5-n),end="", flush=True)
        time.sleep(0.5)
        c()
 
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
    p(random.choice(lootencounters))
    time.sleep(1)
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

    p(f"It's a {lootedItem}!")
    time.sleep(3)
    print(f"{lootedItem} added to inventory.")
    time.sleep(2)
    c()
 
 
# ---------- Player Related ----------
stats = {
    "health": 20,
    "attack": 2,
    "shield": 5,
    "energy": 20,
}
 
inventory = {}
 
 
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
 
 
def player_stats():
    stats_line = Text()
    stats_line.append("♥|", style="bold red")
    stats_line.append(f"{stats['health']}", style="red bold")
    stats_line.append("    ✦ |", style="yellow")
    stats_line.append(f"{stats['energy']}", style="bold yellow")
    stats_line.append("")
    console.print(Panel(stats_line, title="Stats", expand=False,))
 
 
#----------Mob Related------------------
def mobEncounter():
    mobName = random.choice(list(mobs.keys()))
    mob = mobs[mobName]
    p(mob["introPhrase"]["voice1"])
    loadingscreen()
    time.sleep(3)
    p(f"You encountered a {mobName}!")
    while True:
        mobfightMenu(mobName, mob)
        break
 
 
def mobfightMenu(mobName, mob):
    while True:
        p(f"{mobName}\nHealth: {mob['health']}\nAttack: {mob['attack']}")
        print()
        print()
        player_stats()
 
        p("Select an Option:")
        p("1) Fight\n2) Attempt to Flee\n3) View Inventory")
        menuPick = input("> ")
        if menuPick == "1":
            playerAttack(mob)
        elif menuPick == "2":
            risk = random.random()
            if risk < 0.5:
                stats['energy'] -= 1
                console.print("[red]-1 ✦[/red]")
 
 
 
 
# ---------- Walking ----------
def Move():
    loadingscreen()
    encounterChance = random.random()
    if encounterChance < 0.1:
        discoverloot()
    elif encounterChance < 0.35:
        p("Secret Tavern")
    elif encounterChance < 0.75:
        p("Event")
    elif encounterChance < 1:
        mobEncounter()
 
# ---------- Menus ----------
 
def entryMenu():
    p("Select an option")
    p("1] Enter Game")
    p("2] Exit")

    menuPick = ask(["1", "2"])
    if menuPick == "1":
        time.sleep(2)
        c()
        main_playMenu()
    else:
        quit()

def restRoll(): #works with main_playMenu_choice
    number=random.random()
    if number < 0.5:
        p("You slept through the night succesfully.")
    else:
        mobEncounter()
 
 
def main_playMenu(): #Works with main_playMenu_choice, #entryMenu
    moveMenu = Table(box=None)
    moveMenu.add_column(header="Select an Option", header_style="bold cyan")
    moveMenu.add_row("[dim]1)[/dim] Move West")
    moveMenu.add_row("[dim][cyan]2[/cyan])[/dim] [white]Rest[/white]" " [dim](-1+ [yellow]✦[/yellow])[/dim]")
    moveMenu.add_row("[dim]3)[/dim] Inventory")
    moveMenu.add_row("[dim]4)[/dim] Exit")
    console.print(moveMenu)
    menuPick = ask(["1", "2", "3", "4"])
    if menuPick=="1":
        Move()
    elif menuPick=="2":
        restRoll()
    elif menuPick=="3":
        for item,amt in inventory:
            print(item, "|", amt)
    elif menuPick=="4":
        entryMenu()


 
# ---------- Main ----------
 
# === FIX 8 ===
# WAS:  intro(), titlescreen(), the "Good evening" block, AND entryMenu/
#       main_playMenu definitions were all tangled together — some running code
#       sat ABOVE the function definitions it conceptually belonged with, and
#       entryMenu was defined but never actually CALLED, so the game's real
#       entry point never fired.
# NOW:  ALL function definitions live above this line. This bottom block is the
#       ONLY loose, runs-immediately code, and it runs in order:
#         1. intro()        - the cold-open journal
#         2. titlescreen()  - the ASCII title
#         3. greeting       - "Good evening, traveler."
#         4. entryMenu()    - hand control to the menu system, which is what
#                             actually starts the game loop
# WHY:  This is the "definitions up top, one block of running code at the bottom"
#       shape we talked about. By the time this block runs, every function it
#       calls already exists, so order-of-definition can never bite you.
# IF NOT FIXED: entryMenu() was never called, so even with every other bug fixed,
#       the menu system would sit there defined-but-dormant and the game would
#       never reach the play loop. Also, mixing running code between defs is the
#       exact tangle that broke things for you in Stelik.



# intro()
titlescreen()
p("Good evening, traveler.")
time.sleep(2)
c()#Initiailizing
entryMenu()#Pre-Game
loadingscreen()
while True:
    print(player_stats)
    main_playMenu()#Game start prompt

#TODO - Increase time after attacking mobs
#TODO - Have mobs attack player
#TODO - Dont allow mob health to go below 0
#TODO - Start working on randomized events
#TODO - Start on the currency system, possibly implement casino games
#TODO - Add chance for mob to attack player when resting
#TODO - Add food drop chance for defeating mobs, renews health or energy