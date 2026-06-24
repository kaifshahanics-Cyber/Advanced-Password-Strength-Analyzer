# Password Strength Checker

Hello! This repository holds a simple but effective password strength analyzer that I developed. As I study the foundations of system security, I wanted to build a tool that doesn't just say "weak" or "strong," but actually tells the user *why*.

This script evaluates passwords based on five standard security rules: length, capital letters, small letters, numbers, and special symbols.

## What I Learned Building This

* **Boolean Flags:** I learned how to use `True` and `False` variables (`found_upper`, `found_digit`) to act as switches. Once the loop finds a number, the switch flips to `True` so the program knows it met that requirement.
* **Scoring Systems:** I implemented a basic math-based scoring system out of 5. It uses clear `if/elif/else` statements to print the final grade.
* **User-Friendly Output:** I focused heavily on making the print statements look clean and organized using basic text dashes, ensuring the final security report is easy for a normal user to read.
* **Iterating Through Data:** I practiced using `for` loops to check strings character by character, combined with string methods like `.isupper()` and `.isdigit()`.

## How to Run It

1. Make sure Python is installed.
2. Open your command line and run:
```bash
   python password_analyzer.py
