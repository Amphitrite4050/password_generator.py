import string
import random

def generate_password(length, use_digits=True, use_uppercase=True, use_lowercase=True, use_special=True):
    chars = ''
    if use_digits:
        chars += string.digits
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_special:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == '__main__':
    length = 12
    use_digits = True
    use_uppercase = True
    use_lowercase = True
    use_special = True

    password = generate_password(length, use_digits, use_uppercase, use_lowercase, use_special)
    print(password)
