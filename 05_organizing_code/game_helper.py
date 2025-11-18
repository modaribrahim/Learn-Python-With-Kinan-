# Game Helper - Functions for common game tasks
import random

print("🎮 GAME HELPER FUNCTIONS 🎮")
print("Let's create functions we can use in games!")
print()

# Dice rolling function
def roll_dice(sides=6):
    """Roll a die with specified number of sides"""
    return random.randint(1, sides)

# Health calculation function
def calculate_health(level, base_health=100):
    """Calculate health based on character level"""
    return base_health + (level * 20)

# Experience calculation function
def experience_for_next_level(current_level):
    """Calculate experience needed for next level"""
    return current_level * 1000

# Damage calculation function
def calculate_damage(attacker_level, defender_level, base_damage=10):
    """Calculate damage with level advantage"""
    level_diff = attacker_level - defender_level
    damage_modifier = 1 + (level_diff * 0.1)
    final_damage = int(base_damage * damage_modifier)
    return max(1, final_damage)  # Always at least 1 damage

# Random chance function
def random_chance(success_rate=0.5):
    """Return True if random chance succeeds"""
    return random.random() < success_rate

# Display game stats function
def display_character_stats(name, level, health, experience):
    """Display character information in a nice format"""
    print(f"🎭 {name}")
    print(f"   Level: {level}")
    print(f"   Health: {health} ❤️")
    print(f"   Experience: {experience} ⭐")

# Test the functions
print("🧪 Testing our game functions:")
print()

# Character creation demo
character_name = "Hero"
character_level = 3
character_health = calculate_health(character_level)
character_exp = 250

display_character_stats(character_name, character_level, character_health, character_exp)

print("\n⚔️ Combat Demo:")
print(f"Rolling a 6-sided die: {roll_dice()}")
print(f"Rolling a 20-sided die: {roll_dice(20)}")

# Combat simulation
print(f"\nDamage calculation (Level 5 vs Level 3):")
damage = calculate_damage(5, 3)
print(f"Level 5 attacks Level 3: {damage} damage")

print(f"\nDamage calculation (Level 2 vs Level 4):")
damage = calculate_damage(2, 4)
print(f"Level 2 attacks Level 4: {damage} damage")

# Random chance tests
print(f"\n🎲 Random chances:")
print(f"50% chance success: {random_chance(0.5)}")
print(f"25% chance success: {random_chance(0.25)}")
print(f"75% chance success: {random_chance(0.75)}")

print("\n" + "="*40)

# Interactive character creator
print("🎯 Create Your Character!")
name = input("Character name: ")
level = int(input("Starting level (1-10): "))

if 1 <= level <= 10:
    health = calculate_health(level)
    exp_needed = experience_for_next_level(level)

    print(f"\n📋 Your Character:")
    display_character_stats(name, level, health, 0)
    print(f"   Exp needed for next level: {exp_needed}")

    # Test their luck
    print(f"\n🎲 Testing your luck:")
    dice_roll = roll_dice()
    print(f"You rolled a {dice_roll} on a 6-sided die!")

    if dice_roll >= 5:
        print("🎉 Lucky roll! You found a treasure!")
    else:
        print("Keep trying! Practice makes perfect!")

else:
    print("❌ Please enter a level between 1 and 10!")

print("\nGreat job with game functions! 🎉✨")