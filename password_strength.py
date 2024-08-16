import re
def evaluate_password_strength(password):
    score = 0

    # Criteria 1: Length of password
    if len(password) >= 8:
        score += 2
    elif len(password) >= 12:
        score += 3
    else:
        score += 1

    # Criteria 2: Inclusion of numbers
    if re.search(r'\d', password):
        score += 2

    # Criteria 3: Inclusion of symbols
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 2

    # Criteria 4: Variation of character types
    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        score += 3

    return score

# Example usage:
password = "P@ssw0rd123!"
strength = evaluate_password_strength(password)
print(f"Password strength: {strength}/10")
