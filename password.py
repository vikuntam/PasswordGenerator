import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters")

    # Ensure the password has at least one of each character type
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    symbol = random.choice(string.punctuation)

    # Fill the rest of the password length with random choices
    remaining = length - 4
    all_chars = string.ascii_letters + string.digits + string.punctuation
    middle = ''.join(random.choices(all_chars, k=remaining))

    # Combine all and shuffle
    password_list = list(lowercase + uppercase + digit + symbol + middle)
    random.shuffle(password_list)

    return ''.join(password_list)

# Example usage
print("Generated password:", generate_password(16))