# Chapter 7: Object-Oriented Thinking - Classes and Objects 🏗️

## 🎭 Kinan's Story

Kinan's game was getting complex! He had player variables like `player_x`, `player_y`, `player_health`, `player_speed`, and functions like `move_player()`, `draw_player()`, `damage_player()`. "My code is all over the place!" he thought. "Player data and behavior are scattered everywhere. I need a way to bundle them together!"

He discovered **Object-Oriented Programming (OOP)** - a powerful way to create custom data types that bundle data and behavior together into neat, reusable packages called **objects**!

## 🏗️ What is Object-Oriented Programming?

OOP is a way of thinking about programming that organizes code around **objects** rather than actions and data.

### Think About Real Objects
Look around you - a car, a phone, a pen. Each object has:
- **Properties** (data): color, size, model
- **Behaviors** (methods): start, stop, call, write

In programming, we create the same kind of objects!

## 🎯 Classes and Objects

### Class: The Blueprint
A **class** is like a blueprint or template for creating objects.

```python
class Car:
    # This is just the blueprint - no actual car exists yet
    pass
```

### Object: The Actual Thing
An **object** is an actual instance created from a class.

```python
my_car = Car()  # Now we have an actual car object!
your_car = Car()  # Another car object from the same blueprint
```

## 🎮 Creating Your First Class

Now we need to ask ourselves: how can we implement a simple Player class that stores a player's name and health?

### Step 1: The Constructor
Every class needs a special method that runs when you create an object. This is called the **constructor**.

```python
class Player:
    def __init__(self, name, health):
        """This runs when we create a new Player object"""
        self.name = name        # Property: the player's name
        self.health = health    # Property: the player's health
```

**💭 Think about it:** What other properties should a player have? Position? Experience?

### Step 2: Adding Methods
Methods are functions that belong to a class - they define the object's behavior.

Now we might ask: what can a player do? Let's add some basic actions:

```python
def move(self, dx, dy):
    """Move the player"""
    # YOUR TURN: Implement player movement
    # Update x and y position here
    pass  # Remove this and add your implementation

def take_damage(self, amount):
    """Player takes damage"""
    # YOUR TURN: Implement damage logic
    # Subtract damage from health
    # Print what happened
    pass
```

### Step 3: Complete Class Structure
```python
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.x = 0
        self.y = 0

    # YOUR TURN: Implement the move method here
    def move(self, dx, dy):
        pass

    # YOUR TURN: Implement the take_damage method here
    def take_damage(self, amount):
        pass

    def get_status(self):
        """Return player information"""
        return f"{self.name} - Health: {self.health}, Position: ({self.x}, {self.y})"
```

## 🔧 Using Your First Class

Now that we have a Player class, how would we use it?

```python
# Create player objects
hero = Player("Hero", 100)
villain = Player("Villain", 80)

# Test your implementation:
hero.move(5, 3)          # Should move hero to position (5, 3)
hero.take_damage(20)      # Should reduce hero's health

# Use player methods
print(hero.name)          # Should print "Hero"
print(hero.get_status())  # Should show hero's current status
```

## 🎮 Mini Project: Game Character System

Let's build a more complete character system! What do we need for an RPG character?

### Step 1: Enhanced Character Class
We might need to ask ourselves: what makes different character types unique?

```python
class Character:
    def __init__(self, name, char_class, level=1):
        self.name = name
        self.char_class = char_class
        self.level = level
        self.experience = 0

        # YOUR TURN: Set stats based on character class
        # Warriors should have high health and strength
        # Mages should have high mana and intelligence
        # Archers should have good agility and dexterity
        if char_class == "Warrior":
            # YOUR TURN: Set warrior stats
            pass
        elif char_class == "Mage":
            # YOUR TURN: Set mage stats
            pass
        elif char_class == "Archer":
            # YOUR TURN: Set archer stats
            pass

    def display_info(self):
        """Display character information"""
        # YOUR TURN: Print all character information
        pass

    # YOUR TURN: Add an attack method
    def attack(self):
        pass

    # YOUR TURN: Add a level up method
    def level_up(self):
        pass
```

### Step 2: Enemy Class
Every game needs enemies! How would we implement them?

```python
class Enemy:
    def __init__(self, name, difficulty="Normal"):
        self.name = name
        self.difficulty = difficulty

        # YOUR TURN: Set enemy stats based on difficulty
        # Easy: low health, low damage
        # Normal: medium health, medium damage
        # Hard: high health, high damage
        pass

    def display_info(self):
        """Display enemy information"""
        # YOUR TURN: Print enemy stats
        pass

    def attack(self, target):
        """Attack a target"""
        # YOUR TURN: Implement enemy attack
        pass

    def take_damage(self, damage):
        """Take damage"""
        # YOUR TURN: Implement damage logic
        pass
```

### Step 3: Battle System
Now let's tie it all together with a simple battle system:

```python
def battle(player, enemy):
    """Simulate a battle between player and enemy"""
    print(f"\n⚔️ BATTLE: {player.name} vs {enemy.name}!")

    # YOUR TURN: Implement battle logic
    # - Loop until someone is defeated
    # - Player attacks first
    # - Enemy attacks if still alive
    # - Show health status each round
    # - Announce the winner
    pass
```

## 🔗 Inheritance: Creating Specialized Classes

Sometimes we want to create classes that are based on other classes. This is called **inheritance**.

### Basic Inheritance Example
We might ask: how can we create different types of enemies that share common traits?

```python
class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        return 5  # Basic attack damage

# YOUR TURN: Create a Goblin class that inherits from Enemy
# Goblins should have less health but attack faster
class Goblin(Enemy):
    def __init__(self, name):
        # YOUR TURN: Call parent constructor with goblin stats
        pass

    def attack(self):
        # YOUR TURN: Override attack method for goblin
        pass

# YOUR TURN: Create a Dragon class that inherits from Enemy
# Dragons should have much more health and damage
class Dragon(Enemy):
    def __init__(self, name):
        # YOUR TURN: Call parent constructor with dragon stats
        pass

    def attack(self):
        # YOUR TURN: Override attack method for dragon
        pass

    def breathe_fire(self):
        # YOUR TURN: Add special fire attack only dragons have
        pass
```

## 🎮 Interactive Exercises

### Exercise 1: Character Creator
Complete a program that lets users create their own RPG characters:

**Starter Code:**
```python
def create_character():
    name = input("Enter character name: ")
    print("Available classes: Warrior, Mage, Archer")
    char_class = input("Enter character class: ")

    # YOUR TURN: Create the character object
    character = None  # Replace this with your implementation

    # YOUR TURN: Display character information
    character.display_info()

    return character

# Test your character creator
my_character = create_character()
```

### Exercise 2: Monster Collection
Create different monster types and a simple collection system:

```python
# YOUR TURN: Create these monster classes
class Monster:
    def __init__(self, name, rarity):
        # YOUR TURN: Set up monster attributes
        pass

class Dragon(Monster):
    # YOUR TURN: Dragon-specific abilities
    pass

class Slime(Monster):
    # YOUR TURN: Slime-specific abilities
    pass

# YOUR TURN: Create a collection system that:
# - Lets players collect monsters
# - Shows their collection
# - Has different rarity levels
def collect_monsters():
    pass
```

### Exercise 3: RPG Battle Arena
Combine everything into a simple RPG battle system:

```python
# YOUR TURN: Create a complete battle system
def rpg_battle_arena():
    # - Character creation
    # - Enemy encounters
    # - Battle mechanics
    # - Experience and leveling
    # - Victory/defeat conditions
    pass
```

## 🎯 Class Special Methods

Python has special methods that start and end with double underscores (called "dunder methods").

### Magic Methods
Now we might ask: how can we make our objects work better with Python's built-in functions?

```python
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def __str__(self):
        """String representation for print()"""
        # YOUR TURN: Return a nice string description
        return f"Player {self.name} with {self.health} HP"

    def __repr__(self):
        """Developer representation"""
        # YOUR TURN: Return developer-friendly representation
        pass

    def __eq__(self, other):
        """Equality comparison"""
        # YOUR TURN: Check if two players are equal
        pass

    def __gt__(self, other):
        """Greater than comparison (by health)"""
        # YOUR TURN: Compare players by health
        pass
```

## 🎯 Challenges

### Challenge 1: Bank Account System
Think about what classes you'd need for a banking system:
- What properties does a bank account need?
- What actions can you perform on an account?
- How would customers relate to accounts?

```python
# YOUR TURN: Implement these classes
class BankAccount:
    pass

class Customer:
    pass

class Bank:
    pass
```

### Challenge 2: Music Playlist
Think about organizing music:
- What makes up a song?
- How does a playlist work?
- What can a music player do?

```python
# YOUR TURN: Implement these classes
class Song:
    pass

class Playlist:
    pass

class Player:
    pass
```

### Challenge 3: School Management
Think about a school system:
- What information do students have?
- What do teachers do?
- How are courses organized?

```python
# YOUR TURN: Implement these classes
class Student:
    pass

class Teacher:
    pass

class Course:
    pass
```

## 🎯 Challenges

### Challenge 1: Bank Account System
Create classes for:
- `BankAccount` with deposit/withdraw methods
- `Customer` that can have multiple accounts
- `Bank` that manages all customers

### Challenge 2: Music Playlist
Create classes for:
- `Song` with title, artist, duration
- `Playlist` that can add/remove/sort songs
- `Player` that can play/pause/skip songs

### Challenge 3: School Management
Create classes for:
- `Student` with grades and attendance
- `Teacher` with subjects and classes
- `Course` that manages students and assignments

## 🐛 Common OOP Mistakes

### Mistake 1: Forgetting self
```python
class Player:
    def move(self, dx):  # ❌ Missing self parameter
        x += dx  # ❌ Missing self

class Player:
    def move(self, dx):  # ✅ Has self parameter
        self.x += dx  # ✅ Uses self
```

### Mistake 2: Not calling parent constructor
```python
class Enemy(Character):
    def __init__(self, name):  # ❌ Missing parent init
        self.enemy_type = "goblin"

class Enemy(Character):
    def __init__(self, name):
        super().__init__(name)  # ✅ Call parent constructor
        self.enemy_type = "goblin"
```

## 🎉 Chapter Complete!

**Amazing!** You've mastered Object-Oriented Programming! You can now:

- ✅ Create custom data types with classes
- ✅ Bundle data and behavior together in objects
- ✅ Use inheritance to create specialized classes
- ✅ Organize complex game code efficiently
- ✅ Build reusable, maintainable programs
- ✅ Think in terms of objects and their interactions

## 🚀 What's Next?

Kinan was thrilled! His code was now beautifully organized, but everything was still text-based. "How do I create graphics? How do I make visual games?" he wondered.

Join us in Chapter 8: **"Introduction to Pygame - Graphics and Animation"** where Kinan learns to bring his game objects to life with graphics! 🎨✨

---

> 💡 **Pro Tip**: Object-Oriented Programming is how professional games are built. Every character, enemy, item, and game object in modern games is an object. Master OOP, master game development!