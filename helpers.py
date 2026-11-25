import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def generate_user_data():
    email = f'{generate_random_string(5)}@ya.ru'
    password = generate_random_string(7)
    name = generate_random_string(5)
    all_fields = {
        "email": email,
        "password": password,
        "name": name
    }
    return all_fields
