import random
import string
import re 

def generate_password(min_length=8):
    if min_length < 8:
        print("Minimum password length must be at least 8 characters.")
        return None

    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    capital_letter = random.choice(string.ascii_uppercase)

    remaining_length = min_length - 2  
    random_chars = ''.join(random.choice(letters + digits) for _ in range(remaining_length))

    special_char = random.choice(special_chars)

    password = capital_letter + random_chars + special_char

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."

    if not re.search(r"[A-Z]", password):
        return "Weak: Password should contain at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return "Weak: Password should contain at least one lowercase letter."

    if not re.search(r"\d", password):
        return "Weak: Password should contain at least one digit."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Password should contain at least one special character."

    return "Strong: Password meets the criteria for strength."



minimum_length = int(input("Enter the minimum length of the password (at least 8): "))

generated_password = generate_password(minimum_length)
print("Generated Password:", generated_password)

result = check_password_strength(generated_password)
print(result)
