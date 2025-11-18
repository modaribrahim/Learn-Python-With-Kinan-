# Game Inventory System - Practice with lists
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