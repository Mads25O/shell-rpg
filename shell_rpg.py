import random
from classes import Player, Enemies

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
            player.collect_loot(enemy["loot"])
            print(f"You killed a {enemy['name']}! You took {enemy['attack']} damage, gained {enemy['experience']} experience and got {enemy['coins']} coins. Your health: {player.health}")

        elif action == 'heal':
            player.heal(20)
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


