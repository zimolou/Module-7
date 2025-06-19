import random
import string


def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += "!@#$%^&*()"
    
    password = ''.join(random.SystemRandom().choice(chars) for _ in range(length))
    return password

def password_strength(password):
    strength = 0
    if len(password) >= 12: strength += 1
    if any(c.isupper() for c in password): strength += 1 
    if any(c.isdigit() for c in password): strength += 1
    if any(c in "!@#$%^&*()" for c in password): strength += 1
    return min(strength, 4)

def main():
    print("=== Password Generator ===")
    length = int(input("Password length (8-32): ") or 12)
    pw = generate_password(
        length=length,
        use_upper='y' in input("Include uppercase? (y/n): ").lower(),
        use_digits='y' in input("Include digits? (y/n): ").lower(),
        use_special='y' in input("Include special chars? (y/n): ").lower()
    )
    
    print("\nGenerated Password:", pw)
    print("Strength:", "★" * password_strength(pw))
    
    if input("Copy to clipboard? (y/n): ").lower() == 'y':
        pyperclip.copy(pw)
        print("Password copied!")

if __name__ == "__main__":
    main()
