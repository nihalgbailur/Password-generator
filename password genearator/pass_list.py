import random
import string

def generate_password(length):
    password = []
    characters = string.ascii_letters + string.digits + string.punctuation
    for i in range(length):
        password.append(random.choice(characters))
    return ''.join(password)

# Example usage
password = generate_password(12)
print(password)
