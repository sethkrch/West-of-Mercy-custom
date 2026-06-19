############################################################################################
#############################################I M P O R T S##################################
##############################################################################################
import random
from dialogues import lootencounters, buildingencounters, tavernencounters
import time
import os
import json
import pyfiglet
from rich import print as pRich
from rich.highlighter import RegexHighlighter
from rich.theme import Theme
from rich.panel import Panel
from rich.align import Align
from rich.console import Console
from rich.text import Text
from rich.table import Table
console = Console()
with open("mobs.json") as m:
    mobs = json.load(m)
    
class GameHighlighter(RegexHighlighter):
    base_style = "game."          # every style name below is prefixed with this
    highlights = [
        r"(?P<number>\b\d+\b)",   # a run of digits = the "number" group
    ]

game_theme = Theme({
    "game.number": "cyan",        # "base_style" + group name → this style
})

console = Console(highlighter=GameHighlighter(), theme=game_theme)

#############################
#T E X T   F U N C T I O N S#
#############################
def p(text, delay=0.25):
    """Normal text with a short pause after."""
    print(text)
    time.sleep(delay)


def pType(text, style=""):
    """Steady typewriter, flat and even."""
    for char in text:
        console.print(char, end="", style=style)
        time.sleep(0.05)
    time.sleep(0.3)
    print()


def pCentered(text):
    """Print centered."""
    pRich(Align.center(text))


def pDialogue(text):
    """Randomized typing intervals."""
    for char in text:
        console.print(char, end="")

        if char in ".!?":
            time.sleep(random.uniform(0.6, 1.1))      # Pause after sentence
        elif char in ",;:":
            time.sleep(random.uniform(0.25, 0.45))    # Pause after commas
        elif char == " " and random.random() < 0.05:
            time.sleep(random.uniform(0.2, 0.4))      # Random pause after word
        elif random.random() < 0.06:
            time.sleep(random.uniform(0.25, 0.6))     # Random pause
        else:
            time.sleep(random.uniform(0.08, 0.15))    # Normal keypress
    print()


def c():
    """Clear screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


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
    for n in range(6):
        print("●" * n + "○" * (5 - n), end="", flush=True)
        time.sleep(0.35)
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
    pType("\n",random.choice(lootencounters))
    time.sleep(2)
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

    pType(f"\nYou discovered {lootedItem}!")
    time.sleep(2)
    pType(f"\n{lootedItem} added to inventory.")
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
    if stats["health"] <= 0:
        print(pyfiglet.figlet_format("GAME OVER", font="doom"))
        time.sleep(4)
        input("Press any key to continue...")
        quit()
        ##TODO - Add a death screen


def playerAttack(mob, mobName):
    number = random.random()

    pType("\nCharging Attack...")
    time.sleep(5)

    dmg = stats["attack"]
    crit = random.randrange(1, 11)
    if crit in [9, 10] and number < 0.9:
        dmg = dmg * 2
        pType("\nCritical hit!")

    if number < 0.9:

        if mob["shield"] > 0:

            if mob["shield"] > dmg:
                pType(f"\n{mobName} has a shield! {dmg} damage deflected.")
            else:
                pType(f"\nYou broke {mobName}'s shield!")
                mob["shield"] -= dmg

            if mob["shield"] < 0:
                leftovermobhealth = abs(mob["shield"])
                mob["health"] -= abs(mob["shield"])
                mob["shield"] = 0
                if mob["health"] <= 0:
                    return
                pType(f"\nYou dealt {leftovermobhealth}! {mobName} has {mob['health']} remaining.")
                time.sleep(2)

        else:
            mob["health"] -= dmg
            if mob["health"] <= 0:
                return
            pType(f"\nYou dealt {dmg} damage!")
            pType(f"{mobName} has {mob['health']} health remaining.")
            time.sleep(2)
            return

    else:
        pType("\nAttack missed!")
        time.sleep(2)
        return


def mobdeathcheck(mob, mobName):
    if mob["health"] <= 0:
        pType(f"\n{mobName} killed!")
        print("")
        time.sleep(2)
        discoverloot()
        return True


def mobAttack(mob, mobName):
    number = random.random()

    pType(f"\n{mobName} is preparing attack...")
    time.sleep(2)

    dmg = mob["attack"]
    crit = random.randrange(1, 11)
    if crit in [9, 10]:
        dmg = dmg * 2
        pType("\nCritical hit!")
        time.sleep(2)

    if number < 0.9:

        if stats["shield"] > 0:

            if stats["shield"] > dmg:
                stats["shield"] -= dmg
                pType(f"\nYour shield protected you! Shield has {stats['shield']} durability remaining.")
                time.sleep(2)
            else:
                pType(f"\nYour shield is broken!")
                stats["shield"] -= dmg

            if stats["shield"] < 0:
                leftoverdmg = abs(stats["shield"])
                stats["health"] -= abs(stats["shield"])
                stats["shield"] = 0
                if stats["health"] <= 0:
                    return
                pType(f"\n{mobName} dealt {leftoverdmg} damage! You have {stats['health']} health remaining.")
                time.sleep(2)

        else:
            stats["health"] -= dmg
            if stats["health"] <= 0:
                return
            pType(f"\n{mobName} dealt {dmg} damage! You have {stats['health']} health remaining.")
            time.sleep(2)

    else:
        pType("\nAttack missed!")
        time.sleep(2)
        return


def player_stats():
    stats_line = Text()
    stats_line.append("♥|", style="bold red")
    stats_line.append(f"{stats['health']}", style="red bold")
    stats_line.append(f"   ⚔ | ", style="dark_orange")
    stats_line.append(f"{stats['attack']}", style="bold dark_orange")
    stats_line.append("    ⛨ |", style="blue")
    stats_line.append(f"{stats['shield']}", style="bold blue")
    stats_line.append("    ✦ |", style="yellow")
    stats_line.append(f"{stats['energy']}", style="bold yellow")
    stats_line.append("")
    console.print(Panel(stats_line, title="Stats", expand=False))


#----------Mob Related------------------
def mobEncounter():
    mobName = random.choice(list(mobs.keys()))
    mob = mobs[mobName].copy()   # .copy() so beating this mob doesn't damage the master template in mobs.json
    pType(mob["introPhrase"]["voice1"])  ##TODO: Make it select the voices at random
    time.sleep(3)
    pType(f"You encountered {mobName}!")
    time.sleep(2)

    # One fight = one loop. It runs while BOTH are alive, and exits the moment
    # either dies (the `and` becomes false). Fleeing exits early with `return`.
    # ONE clear per lap, right here at the top: the whole previous exchange
    # (your attack + the mob's reply) stacks on screen, then gets wiped in a
    # single sweep when we come back around to redraw the menu.
    while stats["health"] > 0 and mob["health"] > 0:
        c()
        mobstats = Text()
        mobstats.append("♥|", style="bold red")
        mobstats.append(f"{mob['health']}", style="red bold")
        mobstats.append("    ⚔  |", style="blue")
        mobstats.append(f"{mob['attack']}", style="bold blue")
        console.print(Panel(mobstats, title=mobName, expand=False))
        time.sleep(1)
        player_stats()
        time.sleep(1)
        pType("Select an Option:")
        pType("1) Fight\n2) Attempt to Flee\n3) View Inventory")
        menuPick = input("> ")
        time.sleep(1)
        if menuPick == "1":
            playerAttack(mob, mobName)
            if mobdeathcheck(mob, mobName):
                return

            if mob["health"] > 0:
                mobAttack(mob, mobName)
                checkdeath()
        elif menuPick == "2":
            time.sleep(1)
            pType("\nAttempting to flee...")
            time.sleep(2)
            risk = random.random()
            if risk < 0.5:
                stats["energy"] -= 1
                pType("Escape Failed.", style="red")
                pType("-1 ✦", style="red")
                time.sleep(2)
                # no return -> loop continues, still fighting
            else:
                pType("Successfully fled.", style="green")
                time.sleep(2)
                return   # fleeing ends the fight, hands control back to caller
        elif menuPick == "3":
            for item, amt in inventory.items():
                pType(f"{item} | {amt}")
            input("Press any key to continue...")
            c()


# ---------- Walking ----------
def Move():
    if stats["energy"] < 1:
        pType("You don't have enough energy to trek forward.")
        time.sleep(2)
        c()
    else:
        stats["energy"] -= 1
        loadingscreen()
        encounterChance = random.random()
        if encounterChance < 0.01:  ##TODO: make sure you remove the extra 0s when done testing
            discoverloot()
        elif encounterChance < 0.035:
            pType("Secret Tavern")
            time.sleep(2)
        elif encounterChance < 0.075:
            pType("Event")
            time.sleep(2)
        elif encounterChance < 1:
            mobEncounter()


# ---------- Menus ----------

def entryMenu():
    gamestart = Text()
    gamestart.append("Enter '1' to view the tutorial, or press any key to enter the game.", style="magenta")
    gamestart.append("")
    console.print(Panel(gamestart, title="[bold red]West of Mercy[/bold red]", expand=False))
    gamestartpick = input(">")
    if gamestartpick == "1":
        pType("Sorry, no tutorial available yet. Good luck!")
        time.sleep(2)
    else:
        return


def restRoll():  # works with main_playMenu_choice
    pType("You attempt to sleep through the night")
    loadingscreen()
    number = random.random()
    if number < 0.5:
        pType("You slept through the night succesfully.")
        pType("+1 [yellow]energy[/yellow]")
    else:
        time.sleep(2)
        pType("What's that noise?")
        time.sleep(2)
        mobEncounter()


def main_playMenu():
    playMenu = Table(box=None)
    playMenu.add_column(header="Select an Option", header_style="bold cyan")
    playMenu.add_row("[dim][cyan]1[/cyan])[/dim] [white]Move West[/white]" " [dim](-1 [/dim][yellow]✦[/yellow][dim])[/dim]")
    playMenu.add_row("[dim][cyan]2[/cyan])[/dim] [white]Rest[/white]" " [dim](+1 [/dim][yellow]✦[/yellow][dim])[/dim]")
    playMenu.add_row("[dim][cyan]3[/cyan])[/dim] [white]Inventory[/white]")
    playMenu.add_row("[dim][cyan]4[/cyan])[/dim] [white]Exit[/white]")
    console.print(playMenu)
    mP = input("> ")
    return mP


# ---------- Main ----------

# intro()
titlescreen()
pType("Good evening, traveler.")
time.sleep(2)
c()  # Initializing
entryMenu()  # Pre-Game
loadingscreen()
while True:
    checkdeath()
    player_stats()
    mP = main_playMenu()  # Game start prompt
    if mP == "1":
        Move()
    elif mP == "2":
        restRoll()
    elif mP == "3":
        pType("Sorry, this feature is not available yet.")
        time.sleep(2)
    elif mP == "4":
        pType("Thanks for playing!")
        time.sleep(2)
        quit()


#TODO: Increase time after attacking mobs
#TODO: Have mobs attack player
#TODO: Dont allow mob health to go below 0
#TODO: Start working on randomized events
#TODO: Start on the currency system, possibly implement casino games
#TODO: Add chance for mob to attack player when resting
#TODO: Add food drop chance for defeating mobs, renews health or energy
#TODO: Add tutorial