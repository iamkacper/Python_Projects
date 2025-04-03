""" Advanced Password Generator
A script that generates random passwords of a specified length, containing lowercase and uppercase letters, numbers, and special characters to ensure their security. """

import random
import string
import re

def generate_password(length, include_special=True, include_numbers=True, include_uppercase=True, include_lowercase=True):
    # Check for password length
    if length < 8:
        print("Password length should be at least 8 characters for better security.")
        return None

    # Define the character sets for each category
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Create a pool of allowed characters based on user input
    pool = ""
    if include_lowercase:
        pool += lowercase
    if include_uppercase:
        pool += uppercase
    if include_numbers:
        pool += digits
    if include_special:
        pool += special

    # Check if pool is empty (if all categories are excluded)
    if not pool:
        print("At least one character category must be included.")
        return None

    # Ensure that the password contains at least one character from each selected category
    password = []
    if include_lowercase:
        password.append(random.choice(lowercase))
    if include_uppercase:
        password.append(random.choice(uppercase))
    if include_numbers:
        password.append(random.choice(digits))
    if include_special:
        password.append(random.choice(special))

    # Add random characters to fill the remaining length of the password
    password += random.choices(pool, k=length - len(password))

    # Shuffle the password to make it more random
    random.shuffle(password)

    # Return the password as a string
    return ''.join(password)

# Function to check password strength (optional)
def check_password_strength(password):
    # Simple strength checker using regex
    if len(password) < 8:
        return "Weak"
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password) and re.search(r"\d", password) and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Strong"
    return "Moderate"

# Example usage
if __name__ == "__main__":
    password_length = int(input("Enter the desired password length (at least 8): "))
    include_special = input("Include special characters (Y/N)? ").strip().lower() == 'y'
    include_numbers = input("Include numbers (Y/N)? ").strip().lower() == 'y'
    include_uppercase = input("Include uppercase letters (Y/N)? ").strip().lower() == 'y'
    include_lowercase = input("Include lowercase letters (Y/N)? ").strip().lower() == 'y'

    password = generate_password(password_length, include_special, include_numbers, include_uppercase, include_lowercase)

    if password:
        print("Generated password:", password)
        print("Password strength:", check_password_strength(password))