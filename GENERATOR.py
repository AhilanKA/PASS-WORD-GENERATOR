import random
import string

def generate_random_password(length=4):
    characters = string.ascii_letters + string.digits + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

password_length = 4
random_password = generate_random_password(password_length)
print("Random Password:", random_password)
