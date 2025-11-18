# Adventure Choice - Interactive story with if statements
print("🏰 ADVENTURE CHOICE 🏰")
print("You are a brave hero on an important quest!")
print()

# Character setup
hero_name = input("What is your hero's name? ")
print(f"\nWelcome, {hero_name}! Your adventure begins...")
print()

# First decision
print("You stand at a crossroads. Two paths lie before you:")
print("1. The mysterious forest 🌲")
print("2. The dark cave 🗿️")

choice1 = input("Which path do you choose? (1 or 2): ")

if choice1 == "1":
    print("\n🌲 You enter the mysterious forest...")
    print("The trees are ancient and whisper secrets.")

    # Forest adventure
    print("\nSuddenly, you meet a talking owl!")
    print("The owl offers you a choice:")
    print("1. Ask for wisdom")
    print("2. Ask for treasure")

    wisdom_choice = input("What do you ask for? (1 or 2): ")

    if wisdom_choice == "1":
        print("\n🦉 The owl shares ancient wisdom with you!")
        print("You gain knowledge that will help on your quest.")
        print("✨ You feel wiser and more prepared!")
    else:
        print("\n💰 The owl leads you to a hidden treasure!")
        print("You find gold coins and a magic gem!")
        print("✨ You are now rich!")

elif choice1 == "2":
    print("\n🗿️ You enter the dark cave...")
    print("It's dark, but you see a faint light ahead.")

    # Cave adventure
    print("\nYou find a glowing crystal!")
    print("The crystal speaks to you:")
    print("1. Touch the crystal")
    print("2. Leave it alone")

    crystal_choice = input("What do you do? (1 or 2): ")

    if crystal_choice == "1":
        print("\n💎 The crystal gives you magical powers!")
        print("You can now cast simple spells!")
        print("✨ You feel magical energy flow through you!")
    else:
        print("\n🌟 The cave rewards your wisdom!")
        print("You find an ancient artifact left by previous heroes!")
        print("✨ The artifact protects you on your journey!")

else:
    print("\n❌ You decide to think about it longer...")
    print("Sometimes wisdom means knowing when to wait.")
    print("✨ You gain patience!")

# End of adventure
print(f"\n🎭 Congratulations, {hero_name}!")
print("Your adventure was successful!")
print("Every choice you made shaped your unique story!")
print("\nThe End! ✨")