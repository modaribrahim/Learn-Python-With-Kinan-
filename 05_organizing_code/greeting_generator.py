# Greeting Generator - Create reusable greeting functions
print("👋 GREETING GENERATOR 👋")
print("Let's create functions to generate different greetings!")
print()

# Basic greeting function
def simple_greeting(name):
    """Generate a simple greeting"""
    return f"Hello, {name}!"

# Time-based greeting
def time_greeting(name, time_of_day):
    """Generate a greeting based on time of day"""
    greetings = {
        "morning": "Good morning",
        "afternoon": "Good afternoon",
        "evening": "Good evening",
        "night": "Good night"
    }

    time_key = time_of_day.lower()
    if time_key in greetings:
        return f"{greetings[time_key]}, {name}!"
    else:
        return f"Hello, {name}!"

# Enthusiastic greeting
def enthusiastic_greeting(name, excitement_level=1):
    """Generate an enthusiastic greeting"""
    base = f"Hello, {name}"
    exclamation = "!" * excitement_level
    return base + exclamation

# Formal greeting
def formal_greeting(name, title="Mr./Ms."):
    """Generate a formal greeting"""
    return f"Good day, {title} {name}!"

# Character greeting
def character_greeting(name, character_type):
    """Generate a greeting as if from a character"""
    greetings = {
        "pirate": f"Ahoy there, {name}! Arrr!",
        "robot": f"GREETINGS, {name}. I AM A ROBOT.",
        "wizard": f"Welcome, young {name}, to the magical realm!",
        "alien": f"Greetings, Earth-dweller {name}! 👽",
        "cowboy": f"Howdy, {name}! Welcome to the ranch!"
    }

    char_key = character_type.lower()
    if char_key in greetings:
        return greetings[char_key]
    else:
        return f"Hello, {name}!"

# Test the functions
print("🧪 Testing our greeting functions:")
print()

name = "Alex"
print(f"Simple: {simple_greeting(name)}")
print(f"Morning: {time_greeting(name, 'morning')}")
print(f"Afternoon: {time_greeting(name, 'afternoon')}")
print(f"Enthusiastic: {enthusiastic_greeting(name, 3)}")
print(f"Formal: {formal_greeting(name, 'Dr.')}")
print(f"Pirate: {character_greeting(name, 'pirate')}")
print(f"Robot: {character_greeting(name, 'robot')}")

print("\n" + "="*40)

# Interactive greeting generator
print("🎯 Create Your Own Greeting!")
user_name = input("What's your name? ")

print("\nChoose a greeting style:")
print("1. Simple")
print("2. Time-based")
print("3. Enthusiastic")
print("4. Formal")
print("5. Character")

choice = input("Your choice (1-5): ")

if choice == "1":
    greeting = simple_greeting(user_name)
elif choice == "2":
    time = input("What time is it? (morning/afternoon/evening/night): ")
    greeting = time_greeting(user_name, time)
elif choice == "3":
    level = int(input("How enthusiastic? (1-5): "))
    greeting = enthusiastic_greeting(user_name, level)
elif choice == "4":
    title = input("What title? (Mr./Ms./Dr./Prof.): ")
    greeting = formal_greeting(user_name, title)
elif choice == "5":
    print("Available characters: pirate, robot, wizard, alien, cowboy")
    character = input("Choose a character: ")
    greeting = character_greeting(user_name, character)
else:
    greeting = simple_greeting(user_name)

print(f"\n{greeting}")

print("\nGreat job creating functions! 🎉✨")