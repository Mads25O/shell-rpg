

class Player_Actions:
    def __init__(self):
        self.space_and = " & "

    def help():
        print("Uhhh, haven't made it yet, sorry.")

    def profile(self, player):
        print(f"--- Profile for {player.name} ---")
        print(f"Health: {player.health}")
        print(f"Level: {player.level}")
        print(f"Experience: {player.experience}/{player.experience_for_next_level}")
        print(f"Coins: {player.coins}")

    def use_consumable(self, player, action):
        action_split = action.split()
        if len(action_split) > 1 and len(action_split) < 3:
            consumable_name = action_split[1]
            player.use_consumable(consumable_name)
        else:
            print("Usage: use [consumable]")

    def hunt(self, player, enemies):
        enemy = enemies.generate_enemy(player.level)
        player.take_damage(enemy["attack"])
        if player.dead == False:
            player.gain_experience(enemy["experience"])
            player.gain_coins(enemy["coins"])
                    
            print(f"You killed a {enemy['name']}!")
            print(f"Earned {enemy['coins']} coins and {self.space_and.join(f'{amount} {item}' for item, amount in enemy['loot'].items())}.")
            print(f"Gained {enemy['experience']} XP, {player.experience_for_next_level - player.experience} XP until next level.")
            print(f"Lost {enemy['attack']} HP, remaining HP: {player.health}/{player.max_health}")
                    
            player.collect_loot(enemy["loot"])
            player.add_consumable("Apple", 2)

    def buy(self, player):
        pass