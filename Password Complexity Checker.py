import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check digit
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one digit.")

    # Check special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (e.g., !@#$%).")

    # Strength level
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }

# Example usage
print ("Welcome to Sreeram's Password Complexity Checker")
password = input("Enter your password: ")
result = check_password_strength(password)

print(f"\nPassword Strength: {result['strength']}")
if result['feedback']:
    print("Suggestions:")
    for suggestion in result['feedback']:
        print(f"- {suggestion}")
