import random
from classes import Player, Enemies

class Shop:
    def __init__(self):
        pass

    def buy(self):
        pass

    def sell(self):
        pass

class Quests:
    def __init__(self):
        pass


# Mining og fishing
# man kan få sten gennem mining. man får x antal sten baseret på ens pickaxe. % chance for at få ore.
# ore: iron, gold, silver, coal, diamond, emerald.
# ore skal kunne smeltes, og det man får ud af dem kan man bruge til crafting
class Action:
    def __init__(self):
        pass

    def mining(self):
        player = Player()


    def fishing(self):
        pass

    def chopping(self):
        pass

    def farming(self):
        pass

class Crafting:
    def __init__(self):
        pass
# Enemies need to get loaded from json files.
# Their attack vary from monster to monster. Pick random number between min_attack and max_attack.




def main():
    running = True

    player = Player()
    enemies = Enemies()
    #name = input("What is your name? > ")
    name = 'Mads'
    print(f"Welcome to Shell RPG {name}!")
    while running:
        action = input("What do you want to do? > ").lower()

        if action == 'help':
            print("Uhhh, haven't made it yet, sorry.")

        elif action == 'profile':
            print(f"--- Profile for {name} ---")
            print(f"Health: {player.health}")
            print(f"Level: {player.level}")
            print(f"Experience: {player.experience}/{player.experience_for_next_level}")
            print(f"Coins: {player.coins}")
        
        elif action == 'inv' or action == 'inventory':
            player.inventory()

        elif action == 'hunt':
            enemy = enemies.generate_enemy()
            player.take_damage(enemy["attack"])
            player.gain_experience(enemy["experience"])
            player.gain_coins(enemy["coins"])
            print(f"You killed a {enemy["name"]}! You took {enemy["attack"]} damage, gained {enemy["experience"]} experience and got {enemy["coins"]} coins. Your health: {player.health}")

        elif action == 'heal':
            player.heal(10)
            print(f"Healed! Health: {player.health}")

        elif action == 'exit':
            print('Byeeee')
            running = False

        elif action == 'buy':
            print("BOUGHT")
            item = 'apple'
            player.add_item(item)
            
        else:
            print("Don't know what you mean there, buddy. Type 'help' to read all commands.")

if __name__ == '__main__':
    main()


