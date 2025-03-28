import random
import json

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

class Items:
    def __init__(self):
        self.files = {
            "consumables": "consumables.json",
            "resources": "resources.json",
            "weapons": "weapons.json"
        }
        self.item_data = self.load_all_items()

    def load_items(self, file_path):
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: {file_path} not found!")
            return []
        
    def load_all_items(self):
        return {category: self.load_items(file) for category, file in self.files.items()}
    
    def get_item(self, item_name):
        for category, items in self.item_data.items():
            for item in items:
                if item["name"].lower() == item_name.lower():
                    return item
        return None
    
    def get_category_items(self, category):
        return self.item_data.get(category, [])

        

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

class Player:
    def __init__(self):
        self.level = 1
        self.experience = 0
        self.experience_for_next_level = 100
        self.max_health = 100
        self.health = 100
        self.speed = 1
        self.defence = 0
        self.coins = 0

        self.items_manager = Items()
        self.resources =  {}
        self.weapons = {}
        self.consumables = {}
    
    ## RESOURCES ##
    def add_resource(self, resource_name, quantity):
        resource = self.items_manager.get_item(resource_name)
        if resource:
            if resource_name in self.resources:
                self.resources[resource_name]["quantity"] += quantity
            else:
                self.resources[resource_name] = {
                    "quantity" : quantity,
                    "description": resource["description"]
                }
            print(f"Added {quantity} {resource_name}(s) to your inventory.")
        else:
            print(f"{resource_name} not found.")
    
    def add_consumable(self, consumable_name, quantity):
        consumable = self.items_manager.get_item(consumable_name)
        if consumable:
            if consumable_name in self.consumables:
                self.consumables[consumable_name]["quantity"] += quantity
            else:
                self.consumables[consumable_name] = {
                    "quantity" : quantity,
                    "healing": consumable["healing"],
                    "description": consumable["description"]
                }
            print(f"Added {quantity} {consumable_name}(s) to your inventory.")
        else:
            print(f"{consumable_name} not found.")
    
    def use_consumable(self, consumable_name):
        if consumable_name in self.consumables and self.consumables[consumable_name]["quantity"] > 0:
            healing_amount = self.consumables[consumable_name]["healing"]
            self.heal(healing_amount)
            
            self.consumables[consumable_name]["quantity"] -= 1

            print(f"Used {consumable_name}. Health is now {self.health}.")

            if self.consumables[consumable_name]["quantity"] <= 0:
                del self.consumables[consumable_name]
        else:
            print(f"{consumable_name} not found or out of stock.")

    ## WEAPONS ##
    def add_weapon(self, weapon_name):
        weapon = self.items_manager.get_item(weapon_name)
        if weapon:
            if weapon_name in self.weapons:
                print(f"{weapon_name} is already in your inventory.")
            else:
                self.weapons[weapon_name] = {
                    "damage": weapon["damage"],
                    "durability": weapon["durability"],
                    "description": weapon["description"]
                }
                print(f"Added {weapon_name} to your weapons.")
        else:
            print(f"{weapon_name} not found.")

    def remove_weapon(self, weapon_name):
        if weapon_name in self.weapons:
            del self.weapons[weapon_name]
            print(f"Removed {weapon_name} from you inventory.")
        else:
            print(f"{weapon_name} not found in your inventory.")

    def use_weapon(self, weapon_name):
        if weapon_name in self.weapons:
            weapon = self.weapons[weapon_name]
            weapon["durability"] -= 1
            print(f'Used {weapon_name}. Durability now: {weapon["durability"]}.')

            if weapon["durability"] <= 0:
                print(f"{weapon_name} broke!")
                del self.weapons[weapon_name]
        else:
            print(f"{weapon_name} not found.")

    ## INVENTORY ##
    def inventory(self):
        """Display the player's inventory."""
        print("\n--- INVENTORY ---")

        print("\nWeapons:")
        if not self.weapons:
            print("No weapons.")
        else:
            for name, weapon in self.weapons.items():
                damage = weapon["damage"]
                durability = weapon["durability"]
                print(f"{name} - DMG: {damage}, DUR: {durability}")

        print("\nResources:")
        if not self.resources:
            print("No resources.")
        else:
            for resource, quantity in self.resources.items():
                print(f"{resource}: {quantity}")

        print("\nConsumables:")
        if not self.consumables:
            print("No consumables.")
        else:
            for item, quantity in self.consumables.items():
                print(f"{item}: {quantity}")

        print("\n-----------------\n")


    def gain_experience(self, experience):
        self.experience += experience
        if self.experience >= self.experience_for_next_level:
            self.level += 1
            self.experience = 0
            self.experience_for_next_level += 5
            print(f"Gained new level! Now level: {self.level}")

    def gain_coins(self, coins):
        self.coins += coins
    
    ## HEALTH SYSTEM ##
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.death()

    def death(self):
        print("Oh no! You died :(. You lost EVEYTHING!!")
        self.weapons.clear()
        self.resources.clear()
        self.consumables.clear()
        self.coins = 0
    
    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    
        

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


