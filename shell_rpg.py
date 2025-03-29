import random
from classes import Player

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

def monster():
    type = "Zombie"
    attack = random.randint(1, 10)
    experience = random.randint(10, 20)
    coins = random.randint(5, 15)

    return type, attack, experience, coins


def main():
    running = True

    player = Player()
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
            monster_type, damage, experience, coins = monster()
            player.take_damage(damage)
            player.gain_experience(experience)
            player.gain_coins(coins)
            print(f"You killed a {monster_type}! You took {damage} damage, gained {experience} experience and got {coins} coins. Your health: {player.health}")

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


