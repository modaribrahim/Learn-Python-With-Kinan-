# High Score Table - Practice with lists and dictionaries
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

# Main menu
while True:
    print("\n" + "="*40)
    display_scores()

    print("\nOptions:")
    print("1. Add new score")
    print("2. Quit")

    choice = input("Your choice: ")

    if choice == "1":
        add_score()
    elif choice == "2":
        print("👋 Thanks for using the high score table!")
        break
    else:
        print("❌ Invalid choice!")