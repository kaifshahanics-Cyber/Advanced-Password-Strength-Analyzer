# Terminal Password Analyzer 🔐

Hi, I'm Kaif! I am a Second Year Computer Science student from Sindh, Pakistan. I spend most of my time at the local library, focusing on logic building, Python, and mathematics. My ultimate goal is to become a Cybersecurity Expert and Bug Bounty Hunter.

This is an updated version of my early password analyzer project. 

## What makes this version different?
While the core logic remains the same (checking for length, uppercase, lowercase, digits, and symbols without using complex libraries), I updated the user interface. 

Instead of just printing "Weak" or "Strong", the script acts like a real terminal tool. It provides a full security breakdown and tells the user exactly *why* their password is weak by listing out the missing security factors.

## The Logic Behind It:
- **String Loops:** I used a simple `for` loop to scan every single character of the input.
- **Boolean Flags:** I set `has_upper`, `has_lower`, and `has_digit` to `False` initially. When the loop finds a matching character, the flag switches to `True` so the score only increases once per category.
- **Feedback System:** The `if-else` blocks at the end print specific warnings based on which flags remained `False`.

## How to test it:
1. Make sure Python is installed.
2. Run the file: `python "Advance Password Strength Analyzer.py"`
3. Enter a password (try a bad one first, like "apple") and watch the terminal highlight the critical issues!

*Note: I write these scripts from scratch as a way to train my brain for logical problem-solving. It's a stepping stone for my future in cybersecurity. If you are an experienced developer passing by, I'd love to hear your feedback!*
