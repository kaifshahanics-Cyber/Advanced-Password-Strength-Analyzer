# Project: Advanced Password Strength Analyzer
# Developer: Muhammad Kaif Shahani
# Goal: To evaluate password security and prevent brute-force attacks.
# Logic: Checks for length, uppercase, lowercase, numbers, and special characters.

password = input("Set the passwords : ")
score = 0

special_character = ["!","@","#","$","%","^","&"]
if len(password) >= 6:
    score += 1

has_upper = False
has_lower = False
has_digit = False

for i in password:
    if i.isupper() and not has_upper:
        score += 1
        has_upper = True
    elif i.islower() and not has_lower:
        score += 1
        has_lower = True
    elif i.isdigit() and not has_digit:
        score += 1
        has_digit = True

for z in special_character:
    if z in password:
        score += 1
        break
if score >= 4:
    print("\n✓ PASSWORD STRENGTH: EXCELLENT (Very Strong!)")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Current Score: %d/5 Security Factors" % score)
    if len(password) >= 6:
        print("✓ Length Requirements Met")
    else:
        print("✗ Length Requirements Not Met Password too short (Minimum: 6 characters)")
    if has_upper:
        print("✓ Uppercase Characters Detected")
    else:
        print("✗ Missing UPPERCASE letters (A-Z)")
    if has_lower:
        print("✓ Lowercase Characters Detected")
    else:
        print("✗ Missing lowercase letters (a-z)")
    if has_digit:
        print("✓ Numerical Digits Included")
    else:
        print("✗ Add numerical digits (0-9)")
    if any(char in password for char in special_character):
        print("✓ Special Characters Added")
    else:
        print("✗ Missing special characters (!@#$%^&)")
    
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Status: Your password is HIGHLY SECURE!")
    print("Recommendation: Excellent choice for maximum security.\n")
elif score == 3:
    print("\n⚠ PASSWORD STRENGTH: MEDIUM (Moderate Security)")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Current Score: 3/5 Security Factors")
    print("Missing Elements:")
    if len(password) < 6:
        print("  ✗ Password too short (Minimum: 6 characters)")
    if not has_upper:
        print("  • Add UPPERCASE letters (A-Z)")
    if not has_lower:
        print("  • Add lowercase letters (a-z)")
    if not has_digit:
        print("  • Add numerical digits (0-9)")
    if not any(char in password for char in special_character):
        print("  • Add special characters (!@#$%^&)")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Status: Your password is MODERATELY SECURE")
    print("Recommendation: Add missing elements for better protection.\n")
else:
    print("\n✗ PASSWORD STRENGTH: WEAK (Poor Security)")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Current Score: %d/5 Security Factors" % score)
    print("Critical Issues:")
    if len(password) < 6:
        print("  ✗ Password too short (Minimum: 6 characters)")
    if not has_upper:
        print("  ✗ Missing UPPERCASE letters (A-Z)")
    if not has_lower:
        print("  ✗ Missing lowercase letters (a-z)")
    if not has_digit:
        print("  ✗ Missing numerical digits (0-9)")
    if not any(char in password for char in special_character):
        print("  ✗ Missing special characters (!@#$%^&)")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Status: Your password is VULNERABLE")
    print("⚠ WARNING: Do NOT use this password for sensitive accounts!")
    print("Recommendation: Create a stronger password immediately.\n")
