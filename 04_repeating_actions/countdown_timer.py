# Countdown Timer - Practice with for loops
import time

print("🕐 COUNTDOWN TIMER 🕐")
print("Let's count down from 10 to 1!")
print()

# Countdown from 10 to 1
for number in range(10, 0, -1):
    print(f"🚀 {number}...")
    time.sleep(1)  # Wait for 1 second

print("\n🎉 BLAST OFF! 🚀")
print("The countdown is complete!")

# Bonus: Practice with different countdowns
print("\n" + "="*40)
print("Let's try some other countdowns!")

# Count up from 1 to 5
print("\n📈 Counting up:")
for i in range(1, 6):
    print(f"Number {i}")

# Count by 2s
print("\n⚡ Counting by 2s:")
for i in range(0, 11, 2):
    print(f"{i}")

# Spell out a message
print("\n✨ Spelling out 'PYTHON':")
message = "PYTHON"
for letter in message:
    print(letter)

print("\nGreat job practicing loops! 🎯")