import json
import sys
import random

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
        print("YOU DIED! GAME OVER")
        sys.exit()
    
    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

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
        
    def get_random_enemy(self):
        return random.choice(self.all_enemies) if self.all_enemies else None
    
    def generate_enemy(self):
        enemy = self.get_random_enemy()
        return {
            "name": enemy["name"],
            "attack": random.randint(enemy["min_attack"], enemy["max_attack"]),
            "hp": enemy["hp"],
            "experience": random.randint(enemy["min_experience"], enemy["max_experience"]),
            "coins": random.randint(enemy["min_coins"], enemy["max_coins"]),
            "loot": self.get_loot(enemy)

        }
    
    def get_loot(self, enemy):
        max_drops = random.randint(1, 5)
        return random.choices(enemy["loot"], k=max_drops)
        