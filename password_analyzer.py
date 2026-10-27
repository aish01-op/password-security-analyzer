from getpass import getpass


def is_common_password(password):
    with open("common_passwords.txt", "r") as file:
        common_passwords = file.read().splitlines()

    return password.lower() in [p.lower() for p in common_passwords]


def has_repeated_characters(password):
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return True

    return False


def has_sequential_pattern(password):
    password = password.lower()

    sequences = [
        "1234",
        "2345",
        "3456",
        "4567",
        "5678",
        "6789",
        "abcd",
        "bcde",
        "cdef",
        "defg",
        "efgh",
        "qwer",
        "wert",
        "asdf",
        "zxcv"
    ]

    for sequence in sequences:
        if sequence in password:
            return True

    return False


def analyze_password(password):
    print("\nAnalyzing password...")
    print("-" * 50)

    score = 0
    recommendations = []

    # 1. Password length
    length = len(password)

    if length < 8:
        print("Password is too short. It should be at least 8 characters long.")
        recommendations.append("Use at least 8 characters.")
    else:
        print(f"Password length: {length} characters")
        score += 20

    if length >= 12:
        score += 10

    # 2. Uppercase letters
    if any(char.isupper() for char in password):
        print("Password contains uppercase letters.")
        score += 15
    else:
        print("Password does not contain uppercase letters.")
        recommendations.append("Add at least one uppercase letter.")

    # 3. Lowercase letters
    if any(char.islower() for char in password):
        print("Password contains lowercase letters.")
        score += 15
    else:
        print("Password does not contain lowercase letters.")
        recommendations.append("Add at least one lowercase letter.")

    # 4. Numbers
    if any(char.isdigit() for char in password):
        print("Password contains numbers.")
        score += 15
    else:
        print("Password does not contain numbers.")
        recommendations.append("Add at least one number.")

    # 5. Special characters
    has_special = any(not char.isalnum() for char in password)

    if has_special:
        print("Password contains special characters.")
        score += 15
    else:
        print("Password does not contain special characters.")
        recommendations.append("Add at least one special character.")

    # 6. Common password check
    if is_common_password(password):
        print("WARNING: This is a commonly used password.")
        score -= 30
        recommendations.append("Avoid commonly used passwords.")
    else:
        print("Password is not in the common password list.")

    # 7. Repeated character check
    if has_repeated_characters(password):
        print("WARNING: Password contains repeated characters.")
        score -= 15
        recommendations.append(
            "Avoid repeated character patterns such as aaa or 111."
        )
    else:
        print("No repeated character pattern detected.")

    # 8. Sequential pattern check
    if has_sequential_pattern(password):
        print("WARNING: Password contains a predictable sequential pattern.")
        score -= 15
        recommendations.append(
            "Avoid predictable sequences such as 1234 or abcd."
        )
    else:
        print("No sequential pattern detected.")

    # Prevent score from going below zero
    score = max(score, 0)

    # Security score
    print("-" * 50)
    print("Security Score:", score, "/ 100")

    # Password rating
    if score >= 75:
        print("Password Rating: STRONG")
    elif score >= 50:
        print("Password Rating: MEDIUM")
    else:
        print("Password Rating: WEAK")

    # Security recommendations
    print("\nRECOMMENDATIONS")
    print("-" * 50)

    if recommendations:
        for recommendation in recommendations:
            print("- " + recommendation)
    else:
        print("No major weaknesses detected.")
        print("Your password meets all basic security checks.")


def main():
    print("=" * 50)
    print("       PASSWORD SECURITY ANALYZER")
    print("=" * 50)

    password = getpass("Enter password: ")

    analyze_password(password)


if __name__ == "__main__":
    main()
