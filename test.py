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
stats = {
    "health": 20,
    "attack": 2,
    "shield": 5,
    "energy": 20,
}


def pType(text, style=""):
 
    """Steady typewriter, flat and even."""
 
    for char in text:
        console.print(char, end="",style=style)
        time.sleep(0.05)
    time.sleep(0.3)
 
    print()

pType("Run to the store for me", style="bold red")
pType("Run to the other store next", "bold blue")