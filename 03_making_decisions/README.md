# Chapter 3: Making Decisions - If, Elif, and Else 🤔

## 🎭 Kinan's Story

Kinan's programs could remember information, but they always did the same thing every time. "My programs are so boring!" he thought. "I want them to make different choices based on different situations!"

He discovered the power of **conditionals** - like giving his computer a brain that could make decisions!

## 🧠 What Are Conditionals?

Conditionals let your program make choices based on conditions. Think of it like a flowchart:

```
Are you hungry?
    ↓
   YES → Eat food
   NO  → Keep playing games
```

## 🎯 Basic If Statements

The simplest decision structure:

```python
age = 13

if age >= 13:
    print("You can take this course!")
    print("Welcome to Python adventures!")

print("This line always executes")
```

### Comparison Operators

```python
# Equal to
if age == 13:
    print("You're exactly 13!")

# Not equal to
if age != 20:
    print("You're not 20")

# Greater than
if age > 12:
    print("You're a teenager!")

# Less than or equal to
if age <= 18:
    print("You're young and learning!")
```

## 🔄 If-Else: Two Choices

When you have exactly two options:

```python
temperature = 25

if temperature > 30:
    print("It's hot! Stay inside and code! 🌡️")
else:
    print("Perfect weather for outdoor coding! 🌤️")
```

## 🎪 If-Elif-Else: Multiple Choices

When you have many options:

```python
grade = 85

if grade >= 90:
    print("A - Excellent work! 🌟")
elif grade >= 80:
    print("B - Good job! 👍")
elif grade >= 70:
    print("C - Keep trying! 💪")
elif grade >= 60:
    print("D - You can do better!")
else:
    print("F - Let's work together to improve!")
```

## 🎮 Mini Project 1: Quiz Game

```python
# quiz_game.py
print("🧠 PYTHON QUIZ GAME 🧠")
print("Answer these questions about programming!")
print()

score = 0

# Question 1
print("Question 1: What do you call a named storage box in programming?")
answer1 = input("Your answer: ").lower()

if answer1 == "variable":
    print("✅ Correct! Variables store information!")
    score += 10
else:
    print("❌ Wrong! The answer is 'variable'")

# Question 2
print("\nQuestion 2: Python is a...")
print("A) Programming language")
print("B) Type of snake")
print("C) Video game")
answer2 = input("Your answer (A/B/C): ").upper()

if answer2 == "A":
    print("✅ Perfect! Python is a programming language!")
    score += 10
else:
    print("❌ Nope! While pythons are snakes, Python is a programming language!")

# Question 3
print("\nQuestion 3: What symbol do we use for comments in Python?")
answer3 = input("Your answer: ")

if answer3 == "#":
    print("✅ Yes! # starts a comment!")
    score += 10
else:
    print("❌ Wrong! Comments start with #")

# Results
print("\n📊 QUIZ RESULTS 📊")
print("Your score:", score, "out of 30")

if score == 30:
    print("🏆 Perfect! You're a Python master!")
elif score >= 20:
    print("🎉 Great job! You know your stuff!")
elif score >= 10:
    print("👍 Good effort! Keep learning!")
else:
    print("💪 Keep practicing! You'll get there!")
```

## 🔗 Combining Conditions

You can check multiple things at once:

### AND Condition (Both must be true)
```python
age = 15
has_permission = True

if age >= 13 and has_permission:
    print("You can join the coding club!")
```

### OR Condition (Either can be true)
```python
weather = "rainy"
is_coding_time = True

if weather == "sunny" or is_coding_time:
    print("Perfect time to learn Python!")
```

### NOT Condition (Reverses the condition)
```python
game_over = False

if not game_over:
    print("Keep playing!")
```

## 🎮 Mini Project 2: Adventure Game Decisions

```python
# adventure_decisions.py
print("🗺️ CHOOSE YOUR ADVENTURE 🗺️")
print("You're standing at a crossroads...")
print()

player_health = 100
player_gold = 50

# First decision
print("You see two paths:")
print("1. Dark forest (mysterious but potentially rewarding)")
print("2. Sunny meadow (safe but less exciting)")

choice1 = input("Choose your path (1 or 2): ")

if choice1 == "1":
    print("\nYou enter the dark forest...")
    print("You find a treasure chest!")
    treasure_choice = input("Open it? (yes/no): ").lower()

    if treasure_choice == "yes":
        print("💰 You found 100 gold!")
        player_gold += 100
        print("But a trap springs! You lose 20 health.")
        player_health -= 20
    else:
        print("🤔 You decide to leave it. Smart choice!")

elif choice1 == "2":
    print("\nYou walk through the sunny meadow...")
    print("You meet a friendly merchant!")

    if player_gold >= 30:
        buy_choice = input("Buy a health potion for 30 gold? (yes/no): ").lower()
        if buy_choice == "yes":
            player_gold -= 30
            player_health += 50
            print("🧪 You bought a health potion! +50 health")
        else:
            print("You decide to save your gold.")
    else:
        print("The merchant offers you a free apple! +10 health")
        player_health += 10

# Status check
print("\n📊 YOUR STATUS 📊")
print("Health:", player_health)
print("Gold:", player_gold)

if player_health >= 100:
    print("💪 You're in perfect health!")
elif player_health >= 50:
    print("👍 You're feeling good!")
else:
    print("😟 You should be careful!")

if player_gold >= 100:
    print("💰 You're rich!")
    print("🏆 Adventure Complete - Victory!")
else:
    print("💸 Keep collecting gold!")
    print("🎮 Adventure continues...")
```

## 🔍 Complex Conditions

### Nested If Statements
```python
age = 14
has_parent_permission = True
is_member = False

if age >= 13:
    if has_parent_permission:
        if is_member:
            print("Welcome back to the coding club!")
        else:
            print("Welcome to the coding club! Want to become a member?")
    else:
        print("You need parent permission to join!")
else:
    print("Sorry, you need to be 13 or older")
```

### Checking ranges
```python
score = 750

if score >= 0 and score <= 300:
    rank = "Beginner"
elif score > 300 and score <= 700:
    rank = "Intermediate"
elif score > 700 and score <= 1000:
    rank = "Advanced"
else:
    rank = "Expert"

print("Your rank:", rank)
```

## 🎮 Mini Project 3: Smart Calculator

```python
# smart_calculator.py
print("🧮 SMART CALCULATOR 🧮")
print("I can do more than just math!")
print()

# Get user input
first_num = float(input("Enter first number: "))
operation = input("Choose operation (+, -, *, /, %): ")
second_num = float(input("Enter second number: "))

result = 0
operation_name = ""

# Smart decisions based on operation
if operation == "+":
    result = first_num + second_num
    operation_name = "addition"
elif operation == "-":
    result = first_num - second_num
    operation_name = "subtraction"
elif operation == "*":
    result = first_num * second_num
    operation_name = "multiplication"
elif operation == "/":
    if second_num != 0:
        result = first_num / second_num
        operation_name = "division"
    else:
        print("❌ Cannot divide by zero!")
        operation_name = "invalid operation"
elif operation == "%":
    result = first_num % second_num
    operation_name = "modulus (remainder)"
else:
    print("❌ Invalid operation!")
    operation_name = "error"

# Smart feedback on the result
if operation_name != "error" and operation_name != "invalid operation":
    print(f"\n📊 {first_num} {operation} {second_num} = {result}")
    print(f"Operation: {operation_name}")

    # Analyze the result
    if result > 100:
        print("🎉 That's a big number!")
    elif result < 0:
        print("❄️ Negative result! Interesting!")
    elif result == 0:
        print("⭕ Perfect zero!")
    else:
        print("👍 Nice calculation!")

    # Give fun facts
    if result % 2 == 0:
        print("🔢 The result is an even number!")
    else:
        print("🔢 The result is an odd number!")
```

## 🎯 Conditional Challenges

### Challenge 1: Grade Classifier
Create a program that:
- Takes a score from 0-100
- Assigns letter grades A-F
- Gives encouraging messages

### Challenge 2: Weather Adviser
Create a program that:
- Asks for temperature and weather conditions
- Gives clothing advice
- Suggests activities

### Challenge 3: Game Character Validator
Create a program that:
- Validates character creation choices
- Ensures rules are followed
- Gives feedback on character balance

## 🐛 Common Conditional Mistakes

### Mistake 1: Using = instead of ==
```python
age = 15
if age = 13:    # ❌ This assigns 13 to age
    print("Too young!")

if age == 13:   # ✅ This compares age to 13
    print("Perfect age!")
```

### Mistake 2: Forgetting colons
```python
if age > 12     # ❌ Missing colon
    print("Teenager")

if age > 12:    # ✅ Has colon
    print("Teenager")
```

### Mistake 3: Wrong indentation
```python
if age >= 13:
print("Welcome")  # ❌ Not indented

if age >= 13:
    print("Welcome")  # ✅ Properly indented
```

## 🎉 Chapter Complete!

**Incredible!** Your programs can now think! You've mastered:

- ✅ If statements for single conditions
- ✅ If-else for two-way decisions
- ✅ If-elif-else for multiple choices
- ✅ Combining conditions with AND, OR, NOT
- ✅ Nested conditional statements
- ✅ Making smart, responsive programs

## 🚀 What's Next?

Kinan was amazed! His programs could now make intelligent decisions, but they still had to do everything manually. "How can I make my computer repeat actions without writing the same code over and over?" he wondered.

Join us in Chapter 4: **"Loops - The Power of Repetition"** where Kinan discovers how to make his programs work efficiently!

---

> 💡 **Remember**: Conditionals are what make programs "smart." Every decision you make in daily life can be programmed with if-elif-else statements. Think about all the decisions your favorite games make - they're all using conditionals!