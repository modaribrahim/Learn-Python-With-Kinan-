# Quiz Master - Test your knowledge with if statements
print("🧠 PYTHON QUIZ MASTER 🧠")
print("Test your Python knowledge!")
print()

score = 0
total_questions = 3

# Question 1
print("Question 1:")
print("What do we use to print text in Python?")
print("a) print()")
print("b) console.log()")
print("c) echo")

answer1 = input("Your answer (a/b/c): ").lower()

if answer1 == "a":
    print("✅ Correct! print() is used to display text in Python.")
    score += 1
else:
    print("❌ Wrong! The correct answer is a) print()")

print()

# Question 2
print("Question 2:")
print("What symbol do we use for comments in Python?")
print("a) //")
print("b) #")
print("c) <!-- -->")

answer2 = input("Your answer (a/b/c): ").lower()

if answer2 == "b":
    print("✅ Correct! # is used for comments in Python.")
    score += 1
else:
    print("❌ Wrong! The correct answer is b) #")

print()

# Question 3
print("Question 3:")
print("Which of these is a valid variable name in Python?")
print("a) 2cool")
print("b) my-var")
print("c) my_name")

answer3 = input("Your answer (a/b/c): ").lower()

if answer3 == "c":
    print("✅ Correct! my_name follows Python variable naming rules.")
    score += 1
else:
    print("❌ Wrong! The correct answer is c) my_name")

print()
print("=" * 40)
print(f"📊 Your score: {score}/{total_questions}")

# Grade the performance
if score == total_questions:
    print("🏆 PERFECT SCORE! You're a Python master!")
elif score >= total_questions // 2:
    print("👍 Good job! You're learning well!")
else:
    print("📚 Keep practicing! You'll get better!")

print()
print("Thanks for taking the quiz! 🎉")