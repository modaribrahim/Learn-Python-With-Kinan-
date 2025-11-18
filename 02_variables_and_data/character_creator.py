# Character Creator - Learn about variables!
print("🎮 CHARACTER CREATOR 🎮")
print("Let's create your game character!")
print()

# Character basic info
char_name = input("What's your character's name? ")
char_class = input("What class? (Warrior/Mage/Archer) ")
char_level = int(input("What level? (1-10): "))

# Character stats
health_points = 100 + (char_level * 20)
mana_points = 50 + (char_level * 10)
experience_needed = char_level * 500

print()
print("📋 CHARACTER SHEET 📋")
print("Name:", char_name)
print("Class:", char_class)
print("Level:", char_level)
print("Health:", health_points)
print("Mana:", mana_points)
print("Experience to next level:", experience_needed)

print("\n🎮 Class Features:")
print("Each class has unique abilities!")
print("Your character is ready for adventure!")