# Math Practice - Repeat calculations with loops
print("🔢 MATH PRACTICE TRAINER 🔢")
print("Let's practice math problems!")
print()

# Practice multiplication tables
print("📚 Multiplication Practice")
table_num = int(input("Which multiplication table? (1-12): "))

print(f"\n🎯 Here's the {table_num} times table:")
for i in range(1, 13):
    result = table_num * i
    print(f"{table_num} × {i} = {result}")

print("\n" + "="*40)

# Practice with addition
print("➕ Addition Practice")
print("Let's add numbers from 1 to 10:")

total = 0
for i in range(1, 11):
    total += i
    print(f"Adding {i}: Total so far = {total}")

print(f"\n🏁 Final total: {total}")

print("\n" + "="*40)

# Number patterns
print("🎨 Number Patterns")
print("Let's create some cool patterns!")

# Square numbers
print("\nSquare numbers (1² to 5²):")
for i in range(1, 6):
    square = i * i
    print(f"{i}² = {square}")

# Even and odd numbers
print("\nEven numbers up to 10:")
for i in range(2, 11, 2):
    print(i, end=" ")
print()

print("\nOdd numbers up to 10:")
for i in range(1, 11, 2):
    print(i, end=" ")
print()

print("\nGreat math practice! 🧮✨")