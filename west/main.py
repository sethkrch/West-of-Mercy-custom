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
 
 
 
def pDialogue(text):
 
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

    pType(f"You discovered {lootedItem}!")
    time.sleep(3)
    pType(f"{lootedItem} added to inventory.")
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
 

def checkdeath():
    if stats["health"]<=0:
        print(pyfiglet.figlet_format("GAME OVER", font="doom"))
        time.sleep(4)
        input("Press any key to continue...")
        quit()
        ##TODO - Add a death screen
 
def playerAttack(mob,mobName):
    number=random.random()


    pType("Charging Attack...")
    time.sleep(5)


    dmg = stats["attack"]


    if number < 0.9:

        if mob["shield"] > 0:


            if mob["shield"] > dmg:
                pType(f"{mobName} has a shield! {dmg} damage deflected.")
            else:
                pType(f"You broke {mobName}'s shield!")
                mob["shield"] -= dmg


            if mob["shield"] < 0:
                mob["health"] -= abs(mob["shield"])
                mob["shield"] = 0


        else:
            mob["health"] -= dmg
            if mob["health"]<=0:
                p(f"{mobName} killed!")
                discoverloot()
                time.sleep(5)
                return
            

        print(f"{mobName} has {mob['health']} health remaining!")
        time.sleep(5)
        return

    else:
        p("Attack missed!")
        return
def mobAttack(mob, mobName):
    
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
# mobAttack removed — to be rewritten from scratch.
# When you build it: it takes (mob, mobName), does ONE attack on the player,
# applies damage to stats["health"], and RETURNS. It should NOT call playerAttack
# at the end (that was the old chaining bug). The fight loop in mobEncounter is
# what alternates turns now — mobAttack just does the mob's single turn and returns.


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
    mob = mobs[mobName].copy()   # .copy() so beating this mob doesn't damage the master template in mobs.json
    pType(mob["introPhrase"]["voice1"]) ##TODO: Make it select the voices at random
    loadingscreen()
    time.sleep(3)
    pType(f"You encountered {mobName}!")
    time.sleep(2)
    c()

    # One fight = one loop. It runs while BOTH are alive, and exits the moment
    # either dies (the `and` becomes false). Fleeing exits early with `return`.
    while stats["health"] > 0 and mob["health"] > 0:
        mobstats = Text()
        mobstats.append("♥|", style="bold red")
        mobstats.append(f"{mob['health']}", style="red bold")
        mobstats.append("    ⚔  |", style="blue")
        mobstats.append(f"{mob['attack']}", style="bold blue")
        console.print(Panel(mobstats, title=mobName, expand=False))
        time.sleep(2)
        player_stats()

        p("Select an Option:")
        pType("1) Fight\n2) Attempt to Flee\n3) View Inventory")
        menuPick = input("> ")
        time.sleep(1)
        if menuPick == "1":
            playerAttack(mob, mobName)
            mobAttack(mob, mobName)# >>> The mob's turn goes HERE: call mobAttack(mob, mobName) after the
            # >>> player attacks, but only if the mob is still alive. You decide
            # >>> how/when. Left unwired on purpose so the structure stays yours.
        elif menuPick == "2":
            time.sleep(1)
            pType("Attempting to flee.")
            risk = random.random()
            if risk < 0.5:
                time.sleep(2)
                stats['energy'] -= 1
                console.print("[red]Escape Failed.[/red]")
                console.print("[red]-1 ✦[/red]")
                # no return -> loop continues, still fighting
            else:
                time.sleep(2)
                p("Successfully fled.")
                return   # fleeing ends the fight, hands control back to caller
        elif menuPick == "3":
            for item, amt in inventory.items():
                print(item, "|", amt)

    # If we fall out of the loop here, someone died (not fled).
    # TODO: award loot if the MOB died; that logic can live here.
 
 
 
 
# ---------- Walking ----------
def Move():
    loadingscreen()
    encounterChance = random.random()
    if encounterChance < 0.01:##TODO: make sure you remove the extra 0s when done testing
        discoverloot()
    elif encounterChance < 0.035:
        p("Secret Tavern")
    elif encounterChance < 0.075:
        p("Event")
    elif encounterChance < 1:
        mobEncounter()

# ---------- Menus ----------
 
def entryMenu():
    gamestart=Text()
    gamestart.append("Enter '1' to view the tutorial, or press any key to enter the game.", style="magenta")
    gamestart.append("")
    console.print(Panel(gamestart, title="[bold red]West of Mercy[/bold red]", expand=False))
    gamestartpick=input(">")
    if gamestartpick=="1":
        p("Sorry, no tutorial available yet. Good luck!")
        time.sleep(3)
    else:
        return


def restRoll(): #works with main_playMenu_choice
    number=random.random()
    if number < 0.5:
        p("You slept through the night succesfully.")
    else:
        mobEncounter()
 
 
def main_playMenu():
    playMenu = Table(box=None)
    playMenu.add_column(header="Select an Option", header_style="bold red")
    playMenu.add_row("[dim][cyan]1[/cyan])[/dim] [white]Move West[/white]" " [dim](-1 [yellow]✦[/yellow][/dim]")
    playMenu.add_row("[dim][cyan]2[/cyan])[/dim] [white]Rest[/white]" " [dim](+1 [yellow]✦[/yellow])[/dim]")
    playMenu.add_row("[dim][cyan]3[/cyan])[/dim] Inventory")
    playMenu.add_row("[dim][cyan]4[cyan])[/dim] Exit")
    console.print(playMenu)
    mP=input("> ")
    return mP



 
# ---------- Main ----------



# intro()
titlescreen()
p("Good evening, traveler.")
time.sleep(2)
c()#Initiailizing
entryMenu()#Pre-Game
loadingscreen()
while True:
    player_stats()
    mP=main_playMenu()#Game start prompt
    if mP=="1":
        Move()
    elif mP=="2":
        restRoll()


#TODO: Increase time after attacking mobs
#TODO: Have mobs attack player
#TODO: Dont allow mob health to go below 0
#TODO: Start working on randomized events
#TODO: Start on the currency system, possibly implement casino games
#TODO: Add chance for mob to attack player when resting
#TODO: Add food drop chance for defeating mobs, renews health or energy
#TODO: Add tutorial