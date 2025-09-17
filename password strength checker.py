import re

def check_password_strength(password: str) -> str:
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1
    
    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1

    # Digit check
    if re.search(r"[0-9]", password):
        score += 1

    # Symbol check
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1

    # Strength label
    if score <= 1:
        return "Very Weak"
    elif score == 2:
        return "Weak"
    elif score == 3:
        return "Medium"
    elif score == 4:
        return "Strong"
    else:
        return "Very Strong"

# Example
pwd = input("Enter password: ")
print("Password Strength:", check_password_strength(pwd))
