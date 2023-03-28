import random
import string

class PasswordGenerator:
    def __init__(self, length):
        self.length = length

    def generate_password(self):
        password = []
        for i in range(self.length):
            password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
        return ''.join(password)

# Example usage
password_generator = PasswordGenerator(12)
print(password_generator.generate_password())
