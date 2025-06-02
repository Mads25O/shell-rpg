import random
from classes import Player, Enemies
from actions import Player_Actions

def main():
    running = True

    player = Player()
    enemies = Enemies()
    player_actions = Player_Actions()
    start = True
    
    while running:
        if start == True:
            #name = input("What is your name? > ")
            name = 'Mads'
            player.name = name
            print(f"Welcome to Shell RPG {name}!")
            print(f"To get started, write 'help'")
            start = False

        elif player.dead == True:
            try_again = input("Do you want to try again? - Yes / No -\n> ")
            if try_again == 'yes' or try_again == 'y':
                player.reset()
                start = True
            elif try_again == 'no' or try_again == 'n':
                running = False
        
        else:
            action = input("What do you want to do? > ").lower()

            if action == 'help':
                player_actions.help()

            elif action == 'profile':
                player_actions.profile(player)
            
            elif action == 'inv' or action == 'inventory':
                player.inventory()

            elif action == 'hunt':
                player_actions.hunt(player, enemies)

            elif action.startswith('use'):
                player_actions.use_consumable(player, action)

            elif action == 'exit':
                running = False

            elif action == 'buy':
                player_actions.buy(player)
                
            else:
                print("Don't know what you mean there, buddy. Type 'help' to read all commands.")
    
    print('Byeeee')

if __name__ == '__main__':
    main()


