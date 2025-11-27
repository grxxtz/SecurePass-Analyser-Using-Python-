SPECIAL_CHARACTERS = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

def analyze_password(password):
    results = {
        "length_ok": False,
        "has_upper": False,
        "has_lower": False,
        "has_digit": False,
        "has_special": False
    }

    results["length_ok"] = len(password) >= 8

    for char in password:
        if char.isupper():
            results["has_upper"] = True
        elif char.islower():
            results["has_lower"] = True
        elif char.isdigit():
            results["has_digit"] = True
        elif char in SPECIAL_CHARACTERS:
            results["has_special"] = True

    return results


def calculate_strength(result_dict):
    score = sum(result_dict.values())

    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Moderate"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"


def print_report(password, results, strength):
    print("\nPassword Analysis Report")
    print("-" * 40)
    print(f"Password Entered: {password}")
    print(f"Length: {len(password)} characters")

    print("\nCriteria Check:")
    print("-->Minimum Length (8):", results["length_ok"])
    print("--> Uppercase Letter  :", results["has_upper"])
    print("--> Lowercase Letter  :", results["has_lower"])
    print("--> Digit             :", results["has_digit"])
    print("--> Special Character :", results["has_special"])

    print(f"\nPassword Strength: {strength}")


def main():
    print("====== SecurePass Analyzer ======\n")

    while True:
        password = input("Enter your password: ").strip()

        if len(password) == 0:
            print("Password cannot be empty. Try again.\n")
            continue

        results = analyze_password(password)
        strength = calculate_strength(results)

        print_report(password, results, strength)

        choice = input("\nDo you want to check another password? (yes/no): ").lower()
        if choice != "yes":
            print("\nExiting... Stay secure! ")
            break


if __name__ == "__main__":
    main()
