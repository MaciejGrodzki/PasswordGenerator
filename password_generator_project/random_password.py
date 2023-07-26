import random
import string

def generate_password(length, numbers, big, special_characters):
    characters = string.ascii_lowercase
    if big:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if special_characters:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

