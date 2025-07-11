# Password Strength Checker
# Enhancement: Added ability to give users feedback on how to improve their password if it's weak.

LOWER = list("abcdefghijklmnopqrstuvwxyz")
UPPER = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
DIGITS = list("0123456789")
SPECIAL = list("!@#$%^&*()-_=+[]{}|;:\\'\",.<>?/`~")

def word_in_file(word, filename, case_sensitive=False):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                current_word = line.strip()
                if case_sensitive:
                    if word == current_word:
                        return True
                else:
                    if word.lower() == current_word.lower():
                        return True
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return False

def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word):
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

def password_strength(password, min_length=10, strong_length=16):
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0
    
    if word_in_file(password, "topPasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    complexity = word_complexity(password)
    strength = 1 + complexity
    return strength

def main():
    print("Welcome to the Password Strength Checker!")
    while True:
        password = input("Enter a password to check (or 'q' to quit): ")
        if password.lower() == "q":
            print("Goodbye!")
            break

        strength = password_strength(password)
        print(f"Password Strength: {strength} / 5")

        if strength < 3:
            print("Consider making your password longer and using a mix of uppercase, lowercase, numbers, and special characters.")

if __name__ == "__main__":
    main()
