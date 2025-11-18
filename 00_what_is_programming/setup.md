# 🔧 Setting Up Your Programming Workshop

## What You Need to Install

Before we can start our adventure, we need to set up our tools. Don't worry - this is like getting your art supplies ready before painting!

## 1. Install Python 🐍

Python is the language we'll use to talk to computers.

### For Windows:
1. Go to [python.org](https://python.org)
2. Click "Downloads"
3. Download the latest Python version (like Python 3.11 or higher)
4. Run the installer
5. **IMPORTANT**: Check the box that says "Add Python to PATH"

### For Mac:
1. Open Terminal (press Cmd + Space, type "Terminal", press Enter)
2. Type: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
3. Then type: `brew install python3`

### For Linux (Ubuntu/Debian):
1. Open Terminal (press Ctrl + Alt + T)
2. Type: `sudo apt update`
3. Then type: `sudo apt install python3`

## 2. Install a Code Editor 📝

A code editor is like a special notebook for writing code.

### Option 1: VS Code (Recommended)
1. Go to [code.visualstudio.com](https://code.visualstudio.com)
2. Download and install
3. Open VS Code, click Extensions (left sidebar), search for "Python" and install the Python extension

### Option 2: Thonny (Easier for Beginners)
1. Go to [thonny.org](https://thonny.org)
2. Download and install
3. Thonny comes with Python built-in!

## 3. Test Your Setup ✅

Let's make sure everything works!

1. Open your code editor
2. Create a new file
3. Type this exactly:
```python
print("Hello, I'm ready to learn Python!")
```
4. Save it as `test.py`
5. Run it (in VS Code: right-click → "Run Python File in Terminal")

If you see "Hello, I'm ready to learn Python!" in the terminal, you're all set! 🎉

## 🎮 Quick Test: Your First Mini-Program

Let's create a fun test program to make sure everything works:

```python
# This is a comment - Python ignores it!
# Let's see what Python can do:

print("🎮 Welcome to your programming adventure!")
print("Let's do some math:", 2 + 2)
print("Python can even do text magic:", "Kinan" * 3)

# Ask for your name
name = input("What's your name? ")
print("Hello,", name, "! Let's learn Python together! 🚀")
```

## 🔧 Troubleshooting Common Problems

### Problem: "python is not recognized"
**Solution**: Python isn't in your PATH. Try reinstalling and make sure to check "Add Python to PATH" during installation.

### Problem: Nothing happens when I run the code
**Solution**: Make sure you're saving the file with `.py` at the end and actually running it (not just opening it).

### Problem: I see red squiggly lines
**Solution**: That's normal! It's just the editor helping you catch mistakes before you run the code.

## 📁 Setting Up Your Course Folder

Create a folder on your computer called `PythonAdventure` and keep all your projects there. Organize it like this:

```
PythonAdventure/
├── chapter1_first_steps/
├── chapter2_variables/
├── chapter3_decisions/
└── ...
```

## 🎯 You're Ready!

Once you've completed the setup and the test program works, you're ready to start Chapter 1!

Remember: Every professional programmer started exactly where you are now. The most important thing is to start and keep going!

---

> 💡 **Pro Tip**: Don't worry if you don't understand everything in the setup. As long as the test program works, you're ready to learn! We'll explain all the concepts as we go.