import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    """
    Generate a strong random password based on the given criteria.
    
    Parameters:
    - length (int): Length of the password (minimum 4 recommended)
    - use_upper (bool): Include uppercase letters
    - use_lower (bool): Include lowercase letters
    - use_digits (bool): Include digits (0-9)
    - use_special (bool): Include special characters
    
    Returns:
    - str: Generated password
    """
    
    if length < 4:
        print("Warning: It is recommended to have a password length of at least 4 for security.")
    
    character_pool = ""
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation
    
    if not character_pool:
        raise ValueError("At least one character type must be selected.")
    
    # Ensure the password contains at least one character from each selected set
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))
    
    # Fill the rest of the password length with random choices from the pool
    if length > len(password):
        password += random.choices(character_pool, k=length - len(password))
    
    # Shuffle the password list to avoid predictable sequences
    random.shuffle(password)
    
    return ''.join(password)


def main():
    print("🔐 Password Generator 🔐")
    
    try:
        length = int(input("Enter password length (recommended 8 or more): "))
    except ValueError:
        print("Invalid input. Using default length 12.")
        length = 12
    
    use_upper = input("Include uppercase letters? (Y/n): ").strip().lower() != 'n'
    use_lower = input("Include lowercase letters? (Y/n): ").strip().lower() != 'n'
    use_digits = input("Include digits? (Y/n): ").strip().lower() != 'n'
    use_special = input("Include special characters? (Y/n): ").strip().lower() != 'n'
    
    try:
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print(f"\nGenerated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
