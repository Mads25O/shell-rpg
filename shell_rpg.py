import random
from classes import Player, Enemies

def main():
    running = True

    player = Player()
    enemies = Enemies()
    start = True
    
    while running:
        if start == True:
            #name = input("What is your name? > ")
            name = 'Mads'
            print(f"Welcome to Shell RPG {name}!")
            start = False

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
            if player.dead == False:
                player.gain_experience(enemy["experience"])
                player.gain_coins(enemy["coins"])
                
                print(f"You killed a {enemy['name']}!\nEarned {enemy['coins']} coins and items lmao.\nGained {enemy['experience']} XP, {player.experience_for_next_level - player.experience} XP until next level.\nLost {enemy['attack']} HP, remaining HP: {player.health}/{player.max_health}")
                player.collect_loot(enemy["loot"])

            else:
                try_again = input("Do you want to try again? - Yes / No -\n> ")
                if try_again == 'yes' or try_again == 'y':
                    player.reset()
                    start = True
                elif try_again == 'no' or try_again == 'n':
                    running = False

        elif action.startswith('use'):
            action_split = action.split()
            if len(action_split) > 1 and len(action_split) < 3:
                consumable_name = action_split[1]
                player.use_consumable(consumable_name)
            else:
                print("Usage: use [consumable]")

            

        elif action == 'exit':
            running = False

        elif action == 'buy':
            pass
            
        else:
            print("Don't know what you mean there, buddy. Type 'help' to read all commands.")
    
    print('Byeeee')

if __name__ == '__main__':
    main()


