# Game Character System - Practice with classes and objects
import random

class Character:
    """Base class for all game characters"""

    def __init__(self, name, char_class, level=1):
        self.name = name
        self.char_class = char_class
        self.level = level
        self.experience = 0

        # Set stats based on class
        if char_class == "Warrior":
            self.health = 120 + (level * 15)
            self.strength = 15 + (level * 3)
            self.agility = 8 + level
            self.mana = 30 + (level * 2)
        elif char_class == "Mage":
            self.health = 70 + (level * 8)
            self.strength = 6 + level
            self.agility = 10 + (level * 2)
            self.mana = 100 + (level * 15)
        elif char_class == "Rogue":
            self.health = 90 + (level * 10)
            self.strength = 10 + (level * 2)
            self.agility = 15 + (level * 3)
            self.mana = 40 + (level * 3)
        else:
            self.health = 100 + (level * 10)
            self.strength = 10 + level
            self.agility = 10 + level
            self.mana = 50 + (level * 5)

        self.max_health = self.health
        self.max_mana = self.mana
        self.inventory = []

    def display_info(self):
        """Display character information"""
        print(f"\n📋 {self.name} the {self.char_class}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Mana: {self.mana}/{self.max_mana}")
        print(f"Strength: {self.strength}")
        print(f"Agility: {self.agility}")
        print(f"Experience: {self.experience}")
        if self.inventory:
            print(f"Inventory: {', '.join(self.inventory)}")
        else:
            print("Inventory: Empty")

    def attack(self, target):
        """Attack another character"""
        damage = self.strength + random.randint(-3, 3)
        target.take_damage(damage)
        print(f"⚔️ {self.name} attacks {target.name} for {damage} damage!")
        return damage

    def take_damage(self, damage):
        """Take damage from an attack"""
        actual_damage = max(1, damage - (self.agility // 4))  # Agility reduces damage
        self.health -= actual_damage
        return actual_damage

    def use_potion(self):
        """Use a health potion if available"""
        if "Health Potion" in self.inventory:
            self.inventory.remove("Health Potion")
            heal_amount = 30 + (self.level * 5)
            self.health = min(self.health + heal_amount, self.max_health)
            print(f"🧪 {self.name} uses Health Potion! Healed {heal_amount} HP")
            return True
        else:
            print(f"❌ {self.name} has no Health Potions!")
            return False

    def gain_experience(self, amount):
        """Gain experience and check for level up"""
        self.experience += amount
        exp_needed = self.level * 100

        if self.experience >= exp_needed:
            self.level_up()
            return True
        return False

    def level_up(self):
        """Level up the character"""
        self.level += 1
        self.experience = 0

        # Increase stats
        self.max_health += 10 + self.level * 5
        self.health = self.max_health
        self.max_mana += 5 + self.level * 3
        self.mana = self.max_mana
        self.strength += 3
        self.agility += 2

        print(f"🎉 {self.name} leveled up to {self.level}!")

    def add_item(self, item):
        """Add item to inventory"""
        self.inventory.append(item)
        print(f"📦 {self.name} received {item}")

    def is_alive(self):
        """Check if character is still alive"""
        return self.health > 0


class Enemy:
    """Enemy class for game enemies"""

    def __init__(self, name, difficulty="Normal"):
        self.name = name
        self.difficulty = difficulty

        # Set stats based on difficulty
        if difficulty == "Easy":
            self.health = 30
            self.damage = 5
            self.exp_reward = 20
        elif difficulty == "Normal":
            self.health = 50
            self.damage = 8
            self.exp_reward = 35
        elif difficulty == "Hard":
            self.health = 80
            self.damage = 12
            self.exp_reward = 60
        else:
            self.health = 100
            self.damage = 15
            self.exp_reward = 100

        self.max_health = self.health

    def display_info(self):
        """Display enemy information"""
        print(f"\n👹 {self.name} ({self.difficulty})")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Damage: {self.damage}")
        print(f"Experience Reward: {self.exp_reward}")

    def attack(self, target):
        """Attack a target"""
        damage = self.damage + random.randint(-2, 2)
        actual_damage = target.take_damage(damage)
        print(f"🗡️ {self.name} attacks {target.name} for {actual_damage} damage!")
        return actual_damage

    def take_damage(self, damage):
        """Take damage"""
        self.health -= damage
        return damage

    def is_alive(self):
        """Check if enemy is still alive"""
        return self.health > 0


# Game demonstration
print("🎮 GAME CHARACTER SYSTEM DEMO 🎮")
print()

# Create characters
hero = Character("Brave Knight", "Warrior", 3)
mage = Character("Wise Wizard", "Mage", 2)

print("=== CHARACTER CREATION ===")
hero.display_info()
mage.display_info()

# Create enemies
goblin = Enemy("Goblin", "Easy")
orc = Enemy("Orc", "Normal")

print("\n=== ENEMY INFORMATION ===")
goblin.display_info()
orc.display_info()

# Battle simulation
print("\n⚔️ BATTLE SIMULATION ⚔️")

# Hero vs Goblin
print(f"\n{hero.name} vs {goblin.name}!")
while hero.is_alive() and goblin.is_alive():
    hero.attack(goblin)
    if goblin.is_alive():
        goblin.attack(hero)

    print(f"Hero HP: {hero.health}/{hero.max_health} | Goblin HP: {goblin.health}/{goblin.max_health}")

if hero.is_alive():
    print(f"🏆 {hero.name} defeated {goblin.name}!")
    hero.gain_experience(goblin.exp_reward)
else:
    print(f"💀 {hero.name} was defeated by {goblin.name}!")

# Show final character status
print("\n=== FINAL CHARACTER STATUS ===")
hero.display_info()
mage.display_info()

# Add items to inventory
hero.add_item("Sword")
hero.add_item("Health Potion")
mage.add_item("Staff")
mage.add_item("Magic Book")

print("\n=== FINAL STATUS WITH ITEMS ===")
hero.display_info()
mage.display_info()