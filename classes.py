import json
import sys
import random
import math

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
                    return {**item, "category": category}
        return None
    
    def get_category_items(self, category):
        return self.item_data.get(category, [])

class Player:
    def __init__(self):
        self.reset()

    def reset(self):
        self.name = 'Placeholder'
        self.level = 1
        self.experience = 0
        self.experience_for_next_level = 100
        self.max_health = 100
        self.health = 100
        self.speed = 1
        self.defence = 0
        self.coins = 0
        self.dead = False

        self.items_manager = Items()
        self.resources =  {}
        self.weapons = {}
        self.consumables = {}

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
        print("DEAD! GAME OVER")
        self.dead = True
    
    def heal(self, amount):
        if self.health == self.max_health:
            print("Already full health.")
        else:
            self.health += amount
            #healing_applied = amount
            if self.health > self.max_health:
                healing_applied = amount - max(0, self.health - self.max_health)
                self.health = self.max_health
        
        
        return healing_applied

    
    ## ITEMS ##
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
        else:
            print(f"{resource_name} not found.")

    def collect_loot(self, loot_dict):
        for loot_item in loot_dict:
            item_data = self.items_manager.get_item(loot_item)
            if item_data:
                if item_data["category"] == "resources":
                    self.add_resource(loot_item, loot_dict[loot_item])
                elif item_data["category"] == "consumables":
                    self.add_consumable(loot_item, loot_dict[loot_item])
                else:
                    print(f"Warning: {loot_item} has unknown category!")
    
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
        matching_key = next((key for key in self.consumables if key.lower() == consumable_name), None)
        
        if matching_key and self.consumables[matching_key]["quantity"] > 0:
            healing_amount = self.consumables[matching_key]["healing"]
            if healing_amount != 0:
                healing_applied = self.heal(healing_amount)
                print(f"Healed {healing_applied}. Health is now {self.health}.")
            
            self.consumables[matching_key]["quantity"] -= 1
            if self.consumables[matching_key]["quantity"] <= 0:
                del self.consumables[matching_key]
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
            for resource, attributes in self.resources.items():
                print(f"{resource}: {attributes['quantity']} - {attributes['description']}")

        print("\nConsumables:")
        if not self.consumables:
            print("No consumables.")
        else:
            for item, attributes in self.consumables.items():
                print(f"{item}: {attributes['quantity']}")

        print("\n-----------------\n")

class Enemies:
    def __init__(self):
        self.file_path = "enemies.json"
        self.all_enemies = self.load_enemies()
    
    def load_enemies(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: {self.file_path} not found!")
            return []
        
    def get_random_enemy(self, player_level):
        valid_enemies = [
            enemy for enemy in self.all_enemies
            if enemy["player_level_range"][0] <= player_level <= enemy["player_level_range"][1]
        ]
        return random.choice(valid_enemies) if valid_enemies else None
        
    
    def scale_stat(self, base, level, variance=0.1):
        scaled = base * (1 + math.log(level + 1))
        variance_amount = scaled * random.uniform(-variance, variance)
        return int(scaled + variance_amount)
    
    def generate_enemy(self, player_level):
        enemy = self.get_random_enemy(player_level)
        level = random.randint(*enemy["level_range"])

        return {
            "name": enemy["name"],
            "level": level,
            "attack": self.scale_stat(enemy["base_attack"], level),
            "hp": self.scale_stat(enemy["base_hp"], level),
            "experience": self.scale_stat(enemy["base_experience"], level),
            "coins": self.scale_stat(enemy["base_coins"], level),
            "loot": self.get_loot(enemy)

        }
    
    def get_loot(self, enemy):
        max_drops = random.randint(1, 5)
        loot_list = random.choices(enemy["loot"], k=max_drops)
        loot_dict = {key: loot_list.count(key) for key in set(loot_list)}
        return loot_dict
        

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
