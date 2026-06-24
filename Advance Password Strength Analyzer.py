# Project: Password Strength Checker
# Developer: Muhammad Kaif Shahani
# Goal: Check if a password is secure against hackers.

print("--- Password Security Checker ---")
user_password = input("Enter a password to check its strength: ")    

total_score = 0   
special_chars = ["!","@","#","$","%","^","&", "*"]   

# checking length
if len(user_password) >= 6:
    total_score = total_score + 1  

# setting up flag variables
found_upper = False   
found_lower = False   
found_digit = False   

# checking each character one by one
for char in user_password:  
    if char.isupper() and found_upper == False: 
        total_score = total_score + 1  
        found_upper = True 
    
    elif char.islower() and found_lower == False:
        total_score = total_score + 1  
        found_lower = True    
    
    elif char.isdigit() and found_digit == False:
        total_score = total_score + 1 
        found_digit = True

# checking for special characters
for special in special_chars:
    if special in user_password:
        total_score = total_score + 1
        break

# Showing the final results
print("\n--- Your Password Report ---")
print("Score out of 5:", total_score)

if total_score >= 4:
    print("Strength: VERY STRONG")
    print("This is a great password for high security.")
elif total_score == 3:
    print("Strength: MEDIUM")
    print("It is okay, but you can make it better.")
    if found_upper == False:
        print("- Try adding capital letters")
    if found_digit == False:
        print("- Try adding numbers")
else:
    print("Strength: WEAK")
    print("Warning: This password is easy to guess!")
    if len(user_password) < 6:
        print("- Password is too short, make it at least 6 characters")
    if found_upper == False:
        print("- You need capital letters")
    if found_lower == False:
        print("- You need small letters")
    if found_digit == False:
        print("- You need numbers")
