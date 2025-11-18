# Adventure Stats Tracker - Practice with variables
print("🗺️ ADVENTURE TRACKER 🗺️")
print()

# Player progress
player_name = input("Enter your adventurer's name: ")
total_gold = int(input("How much gold do you have? "))
monsters_defeated = int(input("How many monsters defeated? "))
potions_collected = int(input("How many potions collected? "))

# Calculate stats
total_score = (total_gold * 10) + (monsters_defeated * 50) + (potions_collected * 25)

# Calculate monsters per gold (preventing division by zero)
monsters_per_gold = monsters_defeated / max(1, total_gold)  # max() prevents division by zero

# Calculate a simple rank score
rank_score = total_score // 100  # Integer division

print()
print("📊 ADVENTURE SUMMARY 📊")
print("Hero:", player_name)
print("Gold:", total_gold, "coins")
print("Monsters Defeated:", monsters_defeated)
print("Potions:", potions_collected)
print("Total Score:", total_score)
print("Rank Score:", rank_score)
print("Monsters per Gold:", round(monsters_per_gold, 2))

print("\n🎯 Your Adventure Style:")
print("Keep track of these numbers to see your progress!")