# Calculator Functions - Practice with functions
print("🧮 SIMPLE CALCULATOR 🧮")
print("Let's create and use functions!")
print()

# Define basic calculator functions
def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero!"

# Define a helper function
def display_result(operation, num1, num2, result):
    """Display the calculation result in a nice format"""
    print(f"{num1} {operation} {num2} = {result}")

# Test the functions
print("🧪 Testing our functions:")
print()

# Test with example numbers
x, y = 10, 5

result1 = add(x, y)
display_result("+", x, y, result1)

result2 = subtract(x, y)
display_result("-", x, y, result2)

result3 = multiply(x, y)
display_result("×", x, y, result3)

result4 = divide(x, y)
display_result("÷", x, y, result4)

print("\n" + "="*40)

# Interactive calculator
print("🎯 Interactive Calculator")
print("Enter two numbers and choose an operation")

try:
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    print("\nOperations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")

    choice = input("Choose operation (1-4): ")

    if choice == "1":
        result = add(num1, num2)
        display_result("+", num1, num2, result)
    elif choice == "2":
        result = subtract(num1, num2)
        display_result("-", num1, num2, result)
    elif choice == "3":
        result = multiply(num1, num2)
        display_result("×", num1, num2, result)
    elif choice == "4":
        result = divide(num1, num2)
        display_result("÷", num1, num2, result)
    else:
        print("❌ Invalid choice!")

except ValueError:
    print("❌ Please enter valid numbers!")

print("\nGreat job using functions! 🎉✨")