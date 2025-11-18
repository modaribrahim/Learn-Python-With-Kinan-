# Input Collector - Gather multiple inputs with loops
print("📝 INPUT COLLECTOR 📝")
print("Let's collect some information!")
print()

# Collect favorite colors
print("🎨 Favorite Colors")
color_count = int(input("How many favorite colors do you have? "))
colors = []

print("Please enter your favorite colors:")
for i in range(color_count):
    color = input(f"Color {i+1}: ")
    colors.append(color)

print(f"\nYour favorite colors are: {', '.join(colors)}")

print("\n" + "="*40)

# Collect daily activities
print("📅 Daily Activities")
print("What do you do on a typical day?")

activities = []
for time_of_day in ["Morning", "Afternoon", "Evening"]:
    activity = input(f"What do you do in the {time_of_day.lower()}? ")
    activities.append(f"{time_of_day}: {activity}")

print("\n📋 Your Daily Schedule:")
for activity in activities:
    print(f"• {activity}")

print("\n" + "="*40)

# Collect numbers and calculate statistics
print("🔢 Number Statistics")
num_count = int(input("How many numbers do you want to enter? "))
numbers = []

print(f"Enter {num_count} numbers:")
for i in range(num_count):
    while True:
        try:
            num = float(input(f"Number {i+1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("❌ Please enter a valid number!")

# Calculate statistics
if numbers:
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    print(f"\n📊 Statistics:")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")

print("\nGreat job collecting data! 🎯✨")