import random
import time
import os
import pyfiglet
import json
with open("mobs.json") as m:
    mobs=json.load(m)


# # def pt(text):
# #     """Type text like a tired traveler writing in a journal by candlelight."""
# #     for char in text:
# #         print(char, end="", flush=True)

# #         if char in ".!?":
# #             # end of a thought — a heavy, weary beat
# #             time.sleep(random.uniform(0.6, 1.1))
# #         elif char in ",;:":
# #             # a short breath
# #             time.sleep(random.uniform(0.25, 0.45))
# #         elif char == " " and random.random() < 0.05:
# #             # tired hands pausing between words
# #             time.sleep(random.uniform(0.2, 0.4))
# #         elif random.random() < 0.06:
# #             # searching for the next word
# #             time.sleep(random.uniform(0.25, 0.6))
# #         else:
# #             # normal keypress, slow and uneven
# #             time.sleep(random.uniform(0.08, 0.15))
# #     print()          # flat, even speed

# # def pr(text):
# #     for char in text:
# #         print(char, end="", flush=True)
# #         time.sleep(0.05)
    
# # def c(): #Clear Screen
# #     os.system('cls' if os.name == 'nt' else 'clear')


# # def p(text, delay=0.25): #Normal Text
# #     print(text)
# #     time.sleep(delay)

    

# # stats={
# #     "health":20,
# #     "attack":2,
# #     "shield":5,
# #     "energy":20
# # }


# # inventory={
    
# # }

# # monster={
# #     "health":10,
# #     "attack":1,
# #     "shield":0
# # }


# # def intro():
# #     c()
# #     pt("Day 2113")
# #     time.sleep(3)
# #     pt("\rPreacher says the Lord is a shepherd.")
# #     time.sleep(1)
# #     c()
# #     pt("\r I no longer believe myself to be among the kept.")
# #     time.sleep(2)
# #     c()
# #     pt("\rThere is a kind of dark that is not the absence of light, but the absence of anything that light would have shown.")
# #     time.sleep(2.7)
# #     c()
# #     pt("\rMy prayers are met with silence.")
# #     time.sleep(1)
# #     c()
# #     time.sleep(3)


# # lootTable={
# #     "common": {
# #         "Healing" : {
# #             "Cloth wrap" : 2,
# #             "Bandage" : 3
# #         },
        
# #         "Attack" : {
# #             "Rusty Sword" : 3,
# #             "Old Cleaver" : 3,
# #         },
# #     },
    
    
    
    
# #     "uncommon" : {
# #         "Healing" : {
# #             "Antibiotics" : 5,
# #             "Small aid pack" : 7
# #             },
        
# #         "Attack" : {
# #             "Sharpened Iron" : 4,
# #             "Switchblade" : 5,
# #         },
# #         } ,
    
    
    
    
# #     "rare" : {
        
# #         "Healing" : {
# #             "Medical Syringe" : 12,
# #             "Military medkit" : 15
# #             },
        
# #         "Attack" : {
# #             "Longsword" : 9,
# #             "Executioners Blade" : 12,
# #         },
# #         },
    
    
    
    
# #     "legendary" : {
# #         "Healing" : {
# #             "Instant Revive" : 1, #This isnt a "give health" value, it is an amount. If a player dies, but they have one of these, they can continue their journey with full hp
# #             },
# #         "Attack" : {
# #             "Zweihandler" : 16
# #         }
# #         },
# # }

# # def discoverloot():
# #     roll=random.random()
# #     if roll < 0.05:
# #         tier="legendary"
# #     elif roll < 0.15:
# #         tier="rare"
# #     elif roll < 0.30:
# #         tier="uncommon"
# #     else:
# #         tier="common"
        
# #     droptier=random.choice(list(lootTable[tier]))
# #     lootedItem=random.choice(list(lootTable[tier][droptier]))
# #     if lootedItem in inventory:
# #         inventory[lootedItem]+=1
# #     else:
# #         inventory[lootedItem]=1
# #     print(f"+1 {lootedItem} added to inventory.")
    

# # def playerAttack(mob):
# #     dmg=stats["attack"]
# #     if mob["shield"]>0:
# #         if mob["shield"]>dmg:
# #             print(f"Monster has a shield! {dmg} damage deflected.")
# #         else:
# #             print("You broke the monsters shield!")
# #         mob["shield"]-=dmg
# #         if mob["shield"]<0:
# #             mob["health"]-=abs(mob["shield "])
# #             mob["shield"] = 0
# #     else:
# #         mob["health"]-=dmg
# #     print(f"Monster has {mob}['health'] remaining!")

def mobEncounter():
    mob=random.choice(mobs)
    print(mob)
    print(mob["attack"])

mobEncounter()
            

# def multiroll(sides=6, amt=1):
#     exampleList=[]
#     while amt>0:
#         result=random.randint(1, sides)
#         exampleList+=[result]
#         amt-=1
#     return exampleList

# def roll(num1=1, num2=6):
#     x=random.randint(num1, num2)
#     return x

# # def enterroll(exampleList):
# #     counter={}
# #     for i in exampleList:
# #         if i in counter:
# #             counter[i]+=1
# #         else:
# #             counter[i]=1
# #     print(counter)

# walkR=roll()
# print(walkR)
# if walkR in [1, 2, 3]:
#     print("Mob encounter")
# elif walkR in [4, 5]:
#     print("Loot Encounter")
# elif walkR==6:
#     print("Nothing")





# # def duel():
# #     while True:
# #         num=random.randint(1,2)
# #         if num==1:
# #             print("You attack the monster")
# #             playerAttack(monster)
# #             if monster["health"]<=0:
# #                 p("Monster dead.")
# #         else:
# #             print("Monster attacks you!")
# #             attackdmg=monster["attack"]
# #             stats["health"]-=attackdmg



# # # intro()
# # print(pyfiglet.figlet_format("WEST OF MERCY", font="doom"))
# # time.sleep(4)

# # pr("Good evening, traveler.")
# # time.sleep(2)
# # c()
# # p("Select an option")
# # p("1] Head West")
# # p("2] Exit Game")
# # menuPick=input(">")

# # if menuPick=="1":
# #     p("   ----------Stats---------")
# #     p(f" | Health = {stats['health']} | Energy = {stats['energy']} | ")
# #     p("Move Forward (-1 Energy)")
# #     p("Rest (+1 Energy)")
# #     p("View Inventory")
# #     menuPick=input(">")
# #     if menuPick=="1":
# #         stats["energy"]-=1
