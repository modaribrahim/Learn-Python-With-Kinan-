# Chapter 6: Working with Collections - Lists and Dictionaries 📚

## 🎭 Kinan's Story

Kinan's games were getting more complex! He had multiple enemies on screen, items to collect, and player inventories to manage. "I'm creating variables like `enemy1`, `enemy2`, `enemy3`... this is getting messy!" he thought. "There must be a better way to organize groups of related information!"

He discovered **collections** - powerful tools for managing groups of data efficiently! Now instead of 10 separate variables, he could have one neat collection.

## 📋 What Are Collections?

Collections are containers that hold multiple items:
- **Lists**: Ordered collections of items (like a shopping list)
- **Dictionaries**: Key-value pairs of information (like a phone book)
- **Tuples**: Immutable lists (can't be changed once created)
- **Sets**: Collections with no duplicates (like unique game achievements)

## 📦 Lists: Ordered Collections

### Creating Lists
```python
# Empty list
empty_list = []

# List with items
inventory = ["sword", "shield", "potion"]
scores = [100, 85, 92, 78]
mixed = [1, "hello", True, 3.14]

# Using list() constructor
numbers = list([1, 2, 3, 4, 5])
```

### Accessing List Items
```python
inventory = ["sword", "shield", "potion", "map"]

# Indexing starts from 0
first_item = inventory[0]  # "sword"
last_item = inventory[-1]  # "map"

# Slicing
first_two = inventory[0:2]  # ["sword", "shield"]
middle_items = inventory[1:3]  # ["shield", "potion"]
```

### List Methods
```python
inventory = ["sword"]

# Add items
inventory.append("shield")  # ["sword", "shield"]
inventory.insert(0, "map")  # ["map", "sword", "shield"]

# Remove items
inventory.remove("sword")  # ["map", "shield"]
removed_item = inventory.pop()  # Removes last item: "shield"

# Find items
index = inventory.index("map")  # 0
count = inventory.count("shield")  # 0 (shield was removed)

# Sort and reverse
numbers = [3, 1, 4, 1, 5]
numbers.sort()  # [1, 1, 3, 4, 5]
numbers.reverse()  # [5, 4, 3, 1, 1]

# Get length
length = len(inventory)  # 1
```

## 🎮 Mini Project 1: Game Inventory System

```python
# game_inventory.py
print("🎮 RPG INVENTORY SYSTEM 🎮")
print()

# Player inventory
inventory = []
max_items = 10

# Starting items
starting_items = ["sword", "health potion", "map"]
for item in starting_items:
    inventory.append(item)

print(f"Your inventory ({len(inventory)}/{max_items}):")
for i, item in enumerate(inventory, 1):
    print(f"{i}. {item}")

# Game loop for inventory management
while True:
    print("\nWhat would you like to do?")
    print("1. View inventory")
    print("2. Add item")
    print("3. Use item")
    print("4. Drop item")
    print("5. Sort inventory")
    print("6. Quit")

    choice = input("Choice: ")

    if choice == "1":
        print(f"\nInventory ({len(inventory)}/{max_items}):")
        if not inventory:
            print("Your inventory is empty!")
        else:
            for i, item in enumerate(inventory, 1):
                print(f"{i}. {item}")

    elif choice == "2":
        if len(inventory) >= max_items:
            print("❌ Your inventory is full!")
            continue

        item = input("What item do you want to add? ")
        inventory.append(item)
        print(f"✅ Added {item} to inventory!")

    elif choice == "3":
        if not inventory:
            print("❌ Your inventory is empty!")
            continue

        print("Current items:")
        for i, item in enumerate(inventory, 1):
            print(f"{i}. {item}")

        try:
            item_num = int(input("Use item number: ")) - 1
            if 0 <= item_num < len(inventory):
                used_item = inventory.pop(item_num)
                print(f"🧪 Used {used_item}!")
            else:
                print("❌ Invalid item number!")
        except ValueError:
            print("❌ Please enter a valid number!")

    elif choice == "4":
        if not inventory:
            print("❌ Your inventory is empty!")
            continue

        print("Current items:")
        for i, item in enumerate(inventory, 1):
            print(f"{i}. {item}")

        try:
            item_num = int(input("Drop item number: ")) - 1
            if 0 <= item_num < len(inventory):
                dropped_item = inventory.pop(item_num)
                print(f"🗑️ Dropped {dropped_item}!")
            else:
                print("❌ Invalid item number!")
        except ValueError:
            print("❌ Please enter a valid number!")

    elif choice == "5":
        inventory.sort()
        print("✅ Inventory sorted alphabetically!")

    elif choice == "6":
        print("👋 Thanks for managing your inventory!")
        break

    else:
        print("❌ Invalid choice!")
```

## 🗺️ Dictionaries: Key-Value Pairs

### Creating Dictionaries
```python
# Empty dictionary
player_stats = {}

# Dictionary with items
player_stats = {
    "health": 100,
    "mana": 50,
    "strength": 15,
    "agility": 10
}

# Using dict() constructor
enemy = dict(name="Goblin", health=30, damage=5)
```

### Accessing Dictionary Values
```python
player_stats = {"health": 100, "mana": 50, "level": 5}

# Get values
health = player_stats["health"]  # 100
level = player_stats.get("level")  # 5
experience = player_stats.get("experience", 0)  # 0 (default value)

# Change values
player_stats["health"] = 80
player_stats["level"] = 6
```

### Dictionary Methods
```python
player_stats = {"health": 100, "mana": 50, "level": 5}

# Add/Update items
player_stats["experience"] = 250
player_stats.update({"gold": 100, "potions": 3})

# Remove items
removed_health = player_stats.pop("health")  # 100
player_stats.clear()  # Removes all items

# Check if key exists
has_mana = "mana" in player_stats  # True
has_keys = "keys" in player_stats  # False

# Get all keys, values, or items
keys = player_stats.keys()  # dict_keys(['health', 'mana', 'level'])
values = player_stats.values()  # dict_values([100, 50, 5])
items = player_stats.items()  # dict_items([('health', 100), ('mana', 50), ('level', 5)])

# Convert to lists
keys_list = list(player_stats.keys())
items_list = list(player_stats.items())
```

## 🎮 Mini Project 2: Character Database

```python
# character_database.py
print("🗃️ CHARACTER DATABASE 🗃️")
print()

# Database of characters
characters = {}

# Add some starting characters
characters["hero"] = {
    "name": "Brave Knight",
    "class": "Warrior",
    "level": 10,
    "health": 150,
    "mana": 30,
    "strength": 20,
    "agility": 12,
    "inventory": ["sword", "shield", "health potion"]
}

characters["mage"] = {
    "name": "Wise Wizard",
    "class": "Mage",
    "level": 8,
    "health": 80,
    "mana": 120,
    "strength": 8,
    "agility": 10,
    "inventory": ["staff", "magic tome", "mana potion", "health potion"]
}

def display_character(char_id, character):
    print(f"\n📋 {character['name']} ({character['class']})")
    print(f"Level: {character['level']}")
    print(f"Health: {character['health']}")
    print(f"Mana: {character['mana']}")
    print(f"Strength: {character['strength']}")
    print(f"Agility: {character['agility']}")
    print(f"Inventory: {', '.join(character['inventory'])}")

def calculate_power_level(character):
    """Calculate character's total power level"""
    stats_total = character['health'] + character['mana'] + (character['strength'] * 5) + (character['agility'] * 3)
    items_bonus = len(character['inventory']) * 10
    return stats_total + items_bonus

# Main program
while True:
    print("\n" + "="*40)
    print("🎮 CHARACTER DATABASE MENU 🎮")
    print(f"Characters in database: {len(characters)}")

    # List all characters
    if characters:
        print("\nAvailable characters:")
        for i, char_id in enumerate(characters.keys(), 1):
            char_name = characters[char_id]["name"]
            char_level = characters[char_id]["level"]
            power = calculate_power_level(characters[char_id])
            print(f"{i}. {char_name} (Level {char_level}, Power: {power})")

    print("\nOptions:")
    print("1. View character details")
    print("2. Add new character")
    print("3. Level up character")
    print("4. Add item to inventory")
    print("5. Compare characters")
    print("6. Show strongest character")
    print("7. Quit")

    choice = input("\nYour choice: ")

    if choice == "1":
        char_id = input("Enter character ID: ")
        if char_id in characters:
            display_character(char_id, characters[char_id])
        else:
            print("❌ Character not found!")

    elif choice == "2":
        char_id = input("Enter new character ID: ")
        if char_id in characters:
            print("❌ Character ID already exists!")
            continue

        name = input("Character name: ")
        char_class = input("Character class: ")
        level = int(input("Starting level: "))

        characters[char_id] = {
            "name": name,
            "class": char_class,
            "level": level,
            "health": 100 + (level * 10),
            "mana": 50 + (level * 5),
            "strength": 10 + level,
            "agility": 8 + level,
            "inventory": ["starting weapon"]
        }
        print(f"✅ Added {name} to the database!")

    elif choice == "3":
        char_id = input("Enter character ID: ")
        if char_id in characters:
            characters[char_id]["level"] += 1
            characters[char_id]["health"] += 10
            characters[char_id]["mana"] += 5
            characters[char_id]["strength"] += 2
            characters[char_id]["agility"] += 1
            print(f"✅ {characters[char_id]['name']} leveled up to {characters[char_id]['level']}!")
        else:
            print("❌ Character not found!")

    elif choice == "4":
        char_id = input("Enter character ID: ")
        if char_id in characters:
            item = input("Item to add: ")
            characters[char_id]["inventory"].append(item)
            print(f"✅ Added {item} to {characters[char_id]['name']}'s inventory!")
        else:
            print("❌ Character not found!")

    elif choice == "5":
        if len(characters) < 2:
            print("❌ Need at least 2 characters to compare!")
            continue

        print("Available characters:")
        char_ids = list(characters.keys())
        for i, char_id in enumerate(char_ids, 1):
            print(f"{i}. {characters[char_id]['name']}")

        try:
            char1_idx = int(input("First character number: ")) - 1
            char2_idx = int(input("Second character number: ")) - 1

            if 0 <= char1_idx < len(char_ids) and 0 <= char2_idx < len(char_ids):
                char1_id = char_ids[char1_idx]
                char2_id = char_ids[char2_idx]

                char1 = characters[char1_id]
                char2 = characters[char2_id]

                print(f"\n⚔️ BATTLE SIMULATION ⚔️")
                print(f"{char1['name']} vs {char2['name']}")

                power1 = calculate_power_level(char1)
                power2 = calculate_power_level(char2)

                print(f"{char1['name']} Power: {power1}")
                print(f"{char2['name']} Power: {power2}")

                if power1 > power2:
                    print(f"🏆 {char1['name']} would win!")
                elif power2 > power1:
                    print(f"🏆 {char2['name']} would win!")
                else:
                    print("🤝 It's a tie!")
            else:
                print("❌ Invalid character numbers!")
        except ValueError:
            print("❌ Please enter valid numbers!")

    elif choice == "6":
        if not characters:
            print("❌ No characters in database!")
            continue

        strongest_char = max(characters.items(), key=lambda x: calculate_power_level(x[1]))
        power = calculate_power_level(strongest_char[1])
        print(f"\n💪 STRONGEST CHARACTER 💪")
        display_character(strongest_char[0], strongest_char[1])
        print(f"Total Power Level: {power}")

    elif choice == "7":
        print("👋 Thanks for using the character database!")
        break

    else:
        print("❌ Invalid choice!")
```

## 🎯 Working with Lists and Dictionaries Together

### List of Dictionaries
```python
# Multiple game objects
enemies = [
    {"name": "Goblin", "health": 30, "damage": 5},
    {"name": "Orc", "health": 50, "damage": 8},
    {"name": "Dragon", "health": 100, "damage": 15}
]

# Access data
print(enemies[0]["name"])  # "Goblin"
print(enemies[2]["damage"])  # 15

# Modify data
enemies[0]["health"] -= 10  # Goblin takes damage
```

### Dictionary with Lists
```python
# Player with multiple inventories
player = {
    "name": "Hero",
    "health": 100,
    "weapons": ["sword", "bow"],
    "potions": ["health", "mana", "speed"],
    "stats": [15, 10, 8]  # strength, agility, intelligence
}

# Access nested data
print(player["weapons"][0])  # "sword"
print(player["stats"][2])  # 8 (intelligence)
```

## 🎮 Mini Project 3: High Score Table

```python
# high_scores.py
import datetime

print("🏆 HIGH SCORE TABLE 🏆")
print()

# High score database (list of dictionaries)
high_scores = []

# Add some initial scores
high_scores.append({
    "name": "Kinan",
    "score": 1500,
    "level": 10,
    "date": datetime.datetime.now().strftime("%Y-%m-%d")
})

high_scores.append({
    "name": "Player2",
    "score": 1200,
    "level": 8,
    "date": datetime.datetime.now().strftime("%Y-%m-%d")
})

def display_scores():
    """Display all high scores"""
    if not high_scores:
        print("No high scores yet!")
        return

    # Sort by score (highest first)
    sorted_scores = sorted(high_scores, key=lambda x: x["score"], reverse=True)

    print("\n🏆 HIGH SCORES 🏆")
    print("Rank | Name    | Score | Level | Date")
    print("-" * 45)

    for i, entry in enumerate(sorted_scores, 1):
        print(f"{i:4} | {entry['name'][:7]:7} | {entry['score']:5} | {entry['level']:5} | {entry['date']}")

def add_score():
    """Add a new high score"""
    name = input("Enter your name: ")
    try:
        score = int(input("Enter your score: "))
        level = int(input("Enter your level: "))

        new_entry = {
            "name": name,
            "score": score,
            "level": level,
            "date": datetime.datetime.now().strftime("%Y-%m-%d")
        }

        high_scores.append(new_entry)
        print(f"✅ Added score for {name}!")

        # Check if it's a new record
        max_score = max(entry["score"] for entry in high_scores)
        if score == max_score:
            print("🎉 NEW HIGH SCORE! 🎉")

    except ValueError:
        print("❌ Please enter valid numbers for score and level!")

def find_player_scores():
    """Find all scores for a specific player"""
    name = input("Enter player name to search: ")
    player_scores = [entry for entry in high_scores if entry["name"].lower() == name.lower()]

    if not player_scores:
        print(f"No scores found for {name}")
        return

    # Sort by score (highest first)
    player_scores.sort(key=lambda x: x["score"], reverse=True)

    print(f"\n📊 Scores for {name}:")
    for i, entry in enumerate(player_scores, 1):
        print(f"{i}. Score: {entry['score']}, Level: {entry['level']}, Date: {entry['date']}")

def show_statistics():
    """Show high score statistics"""
    if not high_scores:
        print("No scores to analyze!")
        return

    scores = [entry["score"] for entry in high_scores]
    levels = [entry["level"] for entry in high_scores]

    print("\n📈 HIGH SCORE STATISTICS 📈")
    print(f"Total scores: {len(high_scores)}")
    print(f"Highest score: {max(scores)}")
    print(f"Lowest score: {min(scores)}")
    print(f"Average score: {sum(scores) // len(scores)}")
    print(f"Highest level reached: {max(levels)}")
    print(f"Average level: {sum(levels) // len(levels)}")

    # Find top player
    top_entry = max(high_scores, key=lambda x: x["score"])
    print(f"Top player: {top_entry['name']} with {top_entry['score']} points")

# Main menu
while True:
    print("\n" + "="*40)
    display_scores()

    print("\nOptions:")
    print("1. Add new score")
    print("2. Search player scores")
    print("3. Show statistics")
    print("4. Clear all scores")
    print("5. Quit")

    choice = input("Your choice: ")

    if choice == "1":
        add_score()
    elif choice == "2":
        find_player_scores()
    elif choice == "3":
        show_statistics()
    elif choice == "4":
        confirm = input("Are you sure? (yes/no): ").lower()
        if confirm == "yes":
            high_scores.clear()
            print("✅ All scores cleared!")
    elif choice == "5":
        print("👋 Thanks for using the high score table!")
        break
    else:
        print("❌ Invalid choice!")
```

## 🎯 Collection Challenges

### Challenge 1: Recipe Manager
Create a recipe manager using dictionaries where:
- Each recipe has ingredients (list) and instructions (list)
- Users can add, view, and search recipes
- Calculate total ingredients needed for multiple recipes

### Challenge 2: Game Level Editor
Build a level editor using lists of dictionaries:
- Each level has enemies, items, and obstacles
- Save and load levels
- Preview levels before playing

### Challenge 3: Student Gradebook
Create a gradebook system:
- Track students and their grades across subjects
- Calculate averages and rankings
- Generate reports

## 🐛 Common Collection Mistakes

### Mistake 1: Index Out of Range
```python
my_list = [1, 2, 3]
print(my_list[3])  # ❌ Error: index 3 doesn't exist (max is 2)
print(my_list[2])  # ✅ Correct: last element
```

### Mistake 2: Dictionary Key Errors
```python
my_dict = {"name": "Player", "health": 100}
print(my_dict["mana"])  # ❌ Error: key "mana" doesn't exist
print(my_dict.get("mana", 0))  # ✅ Returns 0 if key doesn't exist
```

### Mistake 3: Modifying List While Iterating
```python
my_list = [1, 2, 3, 4, 5]
for item in my_list:  # ❌ This causes problems
    if item % 2 == 0:
        my_list.remove(item)  # Modifying while iterating

for item in my_list[:]:  # ✅ Use slice to create a copy
    if item % 2 == 0:
        my_list.remove(item)
```

## 🎉 Chapter Complete!

**Excellent!** You've mastered collections! Your programs can now:

- ✅ Manage groups of related data with lists
- ✅ Organize information with key-value pairs in dictionaries
- ✅ Combine lists and dictionaries for complex data structures
- ✅ Build inventories, databases, and high score systems
- ✅ Sort, search, and manipulate collections efficiently

## 🚀 What's Next?

Kinan was excited! His programs could now organize complex data, but he was still working with separate variables and functions. "How can I bundle data and behavior together into neat packages?" he wondered.

Join us in Chapter 7: **"Object-Oriented Thinking - Classes and Objects"** where Kinan learns to create his own object types!

---

> 💡 **Pro Tip**: Collections are the backbone of almost every program you'll write. Games use lists for enemies and bullets, dictionaries for player stats and inventories, and combinations of both for complex game data. Master collections, master programming!