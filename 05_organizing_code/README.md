# Chapter 5: Functions - Building Reusable Tools 🛠️

## 🎭 Kinan's Story

Kinan had created many amazing programs, but he faced a new problem: "I keep writing the same code over and over! My calculator math appears in multiple programs. I need a way to reuse my code!"

He discovered **functions** - like building your own reusable tools that you can use anywhere in your programs!

## 🛠️ What Are Functions?

Functions are reusable blocks of code that:
- Have a name
- Can take inputs (parameters)
- Can return outputs
- Can be called multiple times

Think of them like recipes:
```python
# Recipe (Function)
def make_sandwich(bread, filling):
    return f"{bread} sandwich with {filling}"

# Use the recipe multiple times
sandwich1 = make_sandwich("white", "turkey")
sandwich2 = make_sandwich("whole wheat", "peanut butter")
```

## 🎯 Creating Your First Function

### Simple Function
```python
def greet_player():
    print("Welcome to the game!")
    print("Have fun and learn Python!")

# Call the function
greet_player()
greet_player()  # Can call it again!
```

### Function with Parameters
```python
def greet_character(name, level):
    print(f"Hello, {name}!")
    print(f"You're at level {level}, good job!")

greet_character("Kinan", 5)
greet_character("Wizard", 10)
```

### Function with Return Value
```python
def calculate_damage(base_damage, weapon_bonus):
    total_damage = base_damage + weapon_bonus
    return total_damage

damage = calculate_damage(10, 5)
print(f"You dealt {damage} damage!")
```

## 🎮 Mini Project 1: Battle System Functions

```python
# battle_functions.py
import random

def roll_dice(sides=6):
    """Roll a dice with specified number of sides"""
    return random.randint(1, sides)

def calculate_damage(attacker_strength, defender_defense):
    """Calculate damage based on stats"""
    base_damage = attacker_strength - defender_defense
    if base_damage < 1:
        base_damage = 1
    return base_damage

def attack(attacker_name, attacker_strength, defender_name, defender_health):
    """Perform an attack and return new defender health"""
    print(f"\n⚔️ {attacker_name} attacks {defender_name}!")

    # Check if attack hits
    attack_roll = roll_dice(20)
    if attack_roll >= 10:  # 50% chance to hit
        damage = calculate_damage(attacker_strength, 5)
        defender_health -= damage
        print(f"Hit! {defender_name} takes {damage} damage")
        print(f"{defender_name} health: {defender_health}")
    else:
        print("Miss! The attack failed!")

    return defender_health

def check_battle_over(health1, health2, name1, name2):
    """Check if the battle is over and return the winner"""
    if health1 <= 0:
        return name2
    elif health2 <= 0:
        return name1
    else:
        return None

# Battle simulation
print("⚔️ BATTLE SIMULATOR ⚔️")

player_name = input("Enter your character's name: ")
player_health = 100
player_strength = 15

enemy_name = "Goblin"
enemy_health = 50
enemy_strength = 10

turn = 1

while True:
    print(f"\n--- Turn {turn} ---")
    print(f"{player_name}: {player_health} HP | {enemy_name}: {enemy_health} HP")

    # Player turn
    enemy_health = attack(player_name, player_strength, enemy_name, enemy_health)

    # Check if battle is over
    winner = check_battle_over(player_health, enemy_health, player_name, enemy_name)
    if winner:
        print(f"\n🏆 {winner} wins the battle!")
        break

    # Enemy turn
    player_health = attack(enemy_name, enemy_strength, player_name, player_health)

    # Check if battle is over
    winner = check_battle_over(player_health, enemy_health, player_name, enemy_name)
    if winner:
        print(f"\n🏆 {winner} wins the battle!")
        break

    turn += 1

print("Thanks for battling! 🎮")
```

## 📦 Function Types

### Functions That Don't Return Anything
```python
def display_title_screen():
    print("🎮 PYTHON ADVENTURE 🎮")
    print("=" * 25)
    print("1. Start Game")
    print("2. Options")
    print("3. Quit")
    print("=" * 25)

display_title_screen()
```

### Functions That Return Values
```python
def get_player_choice():
    """Get and validate player's menu choice"""
    while True:
        choice = input("Enter your choice (1-3): ")
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice! Please try again.")

player_choice = get_player_choice()
print(f"You chose option {player_choice}")
```

### Functions with Default Parameters
```python
def create_character(name, health=100, level=1):
    """Create a character with default stats"""
    character = {
        "name": name,
        "health": health,
        "level": level,
        "exp": 0
    }
    return character

# Different ways to use the function
hero1 = create_character("Knight")  # Uses all defaults
hero2 = create_character("Mage", health=80)  # Custom health
hero3 = create_character("Archer", health=90, level=3)  # Custom everything
```

## 🎮 Mini Project 2: RPG Character Manager

```python
# rpg_character.py
def display_character(character):
    """Display character information"""
    print(f"\n📋 CHARACTER SHEET 📋")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Health: {character['health']}/{character['max_health']}")
    print(f"Mana: {character['mana']}/{character['max_mana']}")
    print(f"Experience: {character['exp']}")
    print(f"Gold: {character['gold']}")

def level_up(character):
    """Level up a character and improve stats"""
    character['level'] += 1
    character['exp'] = 0
    character['max_health'] += 20
    character['health'] = character['max_health']
    character['max_mana'] += 10
    character['mana'] = character['max_mana']

    print(f"\n🎉 LEVEL UP! 🎉")
    print(f"{character['name']} is now level {character['level']}!")

def gain_experience(character, amount):
    """Add experience and check for level up"""
    character['exp'] += amount
    exp_needed = character['level'] * 100

    print(f"📊 Gained {amount} experience!")

    if character['exp'] >= exp_needed:
        level_up(character)
        return True
    return False

def use_potion(character):
    """Use a health potion if available"""
    if character['potions'] > 0:
        heal_amount = 50
        character['health'] = min(character['health'] + heal_amount, character['max_health'])
        character['potions'] -= 1
        print(f"🧪 Used potion! Healed {heal_amount} HP")
        print(f"Health: {character['health']}/{character['max_health']}")
        return True
    else:
        print("❌ No potions left!")
        return False

# Main game
print("🎮 RPG CHARACTER MANAGER 🎮")

# Create character
name = input("Enter character name: ")
char_class = input("Choose class (Warrior/Mage/Archer): ")

# Initialize character
character = {
    "name": name,
    "class": char_class,
    "level": 1,
    "health": 100,
    "max_health": 100,
    "mana": 50,
    "max_mana": 50,
    "exp": 0,
    "gold": 50,
    "potions": 3
}

print(f"\nWelcome, {character['name']} the {character['class']}!")

# Game loop
while True:
    display_character(character)

    print("\nWhat would you like to do?")
    print("1. Train (gain experience)")
    print("2. Use potion")
    print("3. Shop")
    print("4. Quit")

    choice = input("Choice: ")

    if choice == "1":
        exp_gained = random.randint(20, 50)
        gold_found = random.randint(5, 15)
        character['exp'] += exp_gained
        character['gold'] += gold_found

        print(f"Training complete! +{exp_gained} EXP, +{gold_found} gold")

        # Check for level up
        exp_needed = character['level'] * 100
        if character['exp'] >= exp_needed:
            level_up(character)

    elif choice == "2":
        use_potion(character)

    elif choice == "3":
        if character['gold'] >= 20:
            character['gold'] -= 20
            character['potions'] += 2
            print("💰 Bought 2 potions for 20 gold!")
        else:
            print("❌ Not enough gold! Need 20 gold.")

    elif choice == "4":
        print("Thanks for playing! 👋")
        break

    else:
        print("Invalid choice!")
```

## 🧪 Function Design Tips

### Good Function Names
```python
✅ Good: calculate_damage(), display_health_bar(), is_game_over()
❌ Bad: cd(), dhb(), igo()
```

### Single Responsibility
```python
✅ Good: Each function does one thing well
❌ Bad: One function that does everything
```

### Descriptive Parameters
```python
✅ Good: def attack(attacker_name, damage_amount, target_defense):
❌ Bad: def att(a, d, t):
```

## 🎯 Function Challenges

### Challenge 1: Math Game
Create functions for:
- Generating random math problems
- Checking answers
- Keeping score
- Displaying results

### Challenge 2: Text Adventure
Create functions for:
- Room descriptions
- Player movement
- Item interactions
- Game state management

### Challenge 3: Dice Game
Create a dice game with functions for:
- Rolling different dice
- Calculating scores
- Determining winners
- Game rounds

## 🎉 Chapter Complete!

**Excellent!** You've mastered functions! You can now:

- ✅ Create reusable code blocks
- ✅ Pass data to functions with parameters
- ✅ Return values from functions
- ✅ Use default parameters
- ✅ Organize code into logical units
- ✅ Build complex systems from simple functions

## 🚀 What's Next?

Kinan was thrilled! His code was now organized and reusable, but he needed to manage collections of items. "How do I work with lists of items, like inventory or multiple enemies?" he wondered.

Join us in Chapter 6: **"Working with Collections - Lists and Dictionaries"** where Kinan learns to manage groups of data!

---

> 💡 **Pro Tip**: Functions are the building blocks of all programming. Every game you play, every app you use - they're all built with functions. Master functions, and you can build anything!