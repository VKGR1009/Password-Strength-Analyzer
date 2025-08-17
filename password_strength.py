import re

def check_password_strength(password):
    strength = 0
    remarks = []

    # Length check
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password is too short (use at least 8 characters).")

    # Uppercase, lowercase, digits, symbols
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add lowercase letters.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks.append("Add numbers.")

    if re.search(r"[@$!%*?&]", password):
        strength += 1
    else:
        remarks.append("Add special characters (@, $, !, %, *, ?, &).")

    # Final evaluation
    if strength <= 2:
        rating = "Weak"
    elif strength <= 4:
        rating = "Medium"
    else:
        rating = "Strong"

    return rating, remarks


if __name__ == "__main__":
    pwd = input("Enter a password to test: ")
    rating, feedback = check_password_strength(pwd)
    print(f"\nPassword Strength: {rating}")
    if feedback:
        print("Suggestions:")
        for r in feedback:
            print("-", r)
