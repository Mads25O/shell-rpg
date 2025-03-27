import random

class Shop:
    def __init__(self):
        self.items = {}

    def buy(self):
        pass

def chopping():
    pass

def mining():
    pass

def fishing():
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
        self.items =  {}

    def gain_experience(self, experience):
        self.experience += experience
        if self.experience >= self.experience_for_next_level:
            self.level += 1
            self.experience = 0
            self.experience_for_next_level += 5
            print(f"Gained new level! Now level: {self.level}")

    def gain_coins(self, coins):
        self.coins += coins
    
    def take_damage(self, damage):
        self.health -= damage

        if self.health <= 0:
            self.death()

    def death(self):
        print("Oh no! You died :(. You lost EVEYTHING!!")

    
    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
    


def main():
    running = True

    player = Player()
    name = input("What is your name? > ")
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

        elif action == 'hunt':
            monster_type, damage, experience, coins = monster()
            player.take_damage(damage)
            player.gain_experience(experience)
            player.gain_coins(coins)
            print(f"You killed a {monster_type}! You took {damage} damage, gained {experience} experience and got {coins} coins. Your health: {player.health}")

        elif action == 'heal':
            player.heal(10)
            print(f"Healed! Health: {player.health}")
            
        else:
            print("Don't know what you mean there, buddy. Type 'help' to read all commands.")

    

if __name__ == '__main__':
    main()