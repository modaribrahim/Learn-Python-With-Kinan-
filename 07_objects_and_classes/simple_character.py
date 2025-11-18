# Simple Character Creator - Easy introduction to classes
# Think of classes as BLUEPRINTS for creating objects!

print("🎮 SIMPLE CHARACTER CREATOR 🎮")
print("Learn how classes work by creating game characters!")
print()

# A class is like a blueprint for creating objects
class Character:
    """This is a blueprint for creating game characters"""

    # __init__ is a special method that runs when we create a new character
    def __init__(self, name, character_type):
        """Set up the character when it's created"""
        print(f"Creating a new character named {name}...")

        # These are the character's properties (attributes)
        self.name = name
        self.character_type = character_type
        self.level = 1
        self.health = 100
        self.experience = 0

        # Give different stats based on character type
        if character_type == "Warrior":
            self.strength = 15
            self.defense = 10
            self.special_move = "Power Strike"
        elif character_type == "Mage":
            self.strength = 5
            self.defense = 5
            self.special_move = "Fireball"
        elif character_type == "Archer":
            self.strength = 10
            self.defense = 7
            self.special_move = "Perfect Shot"
        else:
            self.strength = 8
            self.defense = 8
            self.special_move = "Basic Attack"

    def show_info(self):
        """Display character information"""
        print(f"\n📋 CHARACTER CARD:")
        print(f"   Name: {self.name}")
        print(f"   Type: {self.character_type}")
        print(f"   Level: {self.level}")
        print(f"   Health: {self.health}")
        print(f"   Strength: {self.strength}")
        print(f"   Defense: {self.defense}")
        print(f"   Special Move: {self.special_move}")
        print(f"   Experience: {self.experience}")

    def attack(self):
        """Make the character attack"""
        damage = self.strength + 5  # Base damage + strength
        print(f"\n⚔️ {self.name} attacks with {self.special_move}!")
        print(f"   Deals {damage} damage!")
        return damage

    def take_damage(self, damage):
        """Character takes damage"""
        actual_damage = max(1, damage - self.defense)  # Defense reduces damage
        self.health -= actual_damage
        print(f"💔 {self.name} takes {actual_damage} damage!")
        print(f"   Health remaining: {self.health}")

        if self.health <= 0:
            print(f"💀 {self.name} has been defeated!")

    def gain_experience(self, exp_amount):
        """Character gains experience"""
        self.experience += exp_amount
        print(f"✨ {self.name} gains {exp_amount} experience!")
        print(f"   Total experience: {self.experience}")

        # Check if ready to level up (100 exp per level)
        if self.experience >= self.level * 100:
            self.level_up()

    def level_up(self):
        """Character levels up and gets stronger"""
        self.level += 1
        self.experience = 0
        self.health += 20
        self.strength += 3
        self.defense += 2

        print(f"🎉 {self.name} LEVELED UP to level {self.level}!")
        print(f"   Health increased to {self.health}")
        print(f"   Strength increased to {self.strength}")
        print(f"   Defense increased to {self.defense}")

print("=" * 50)
print("DEMO: Creating Characters")
print("=" * 50)

# Create characters using the Character blueprint
hero = Character("Hero", "Warrior")
wizard = Character("Wizard", "Mage")

print("\n" + "=" * 50)
print("CHARACTER INFORMATION")
print("=" * 50)

# Show character information
hero.show_info()
wizard.show_info()

print("\n" + "=" * 50)
print("BATTLE DEMO")
print("=" * 50)

# Battle simulation
print(f"\n⚔️ {hero.name} vs Goblin!")
goblin_damage = hero.attack()
hero.gain_experience(50)

print(f"\n🪄 {wizard.name} casts a spell!")
spell_damage = wizard.attack()
wizard.gain_experience(30)

print("\n" + "=" * 50)
print("LEVELING UP DEMO")
print("=" * 50)

# Make wizard gain more experience to level up
wizard.gain_experience(50)
wizard.gain_experience(50)
wizard.show_info()

print("\n" + "=" * 50)
print("CREATE YOUR OWN CHARACTER!")
print("=" * 50)

# Let the user create their own character
player_name = input("What's your character's name? ")
print("Available types: Warrior, Mage, Archer")
player_type = input("What type of character? (Warrior/Mage/Archer): ")

# Create the player's character
player = Character(player_name, player_type)
player.show_info()

print(f"\n🎮 Your character {player_name} is ready for adventure!")
print("You can now use this character in your own games!")

print("\n" + "=" * 50)
print("WHY CLASSES ARE AWESOME!")
print("=" * 50)

print("""
🎯 Classes help you organize your code by grouping related data and functions together.

📦 Think of it like this:
   - Character = BLUEPRINT (the class)
   - hero, wizard = ACTUAL CHARACTERS (objects)

🎮 Benefits:
   ✅ Reuse the same code for many characters
   ✅ Each character has its own data (health, level, etc.)
   ✅ Easy to add new characters later
   ✅ Keeps your game code organized

🚀 In your games, you can create classes for:
   - Player characters
   - Enemies
   - Items (weapons, potions)
   - Game objects (bullets, powerups)

Now you understand the basics of classes! Keep practicing!
""")