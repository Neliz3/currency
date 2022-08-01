import random
import string


def generate_address(amount: int = 10):
    box = ''

    for _ in range(amount):
        chars = string.ascii_letters + string.digits
        address = ''

        # Generating a first part of email
        for _ in range(random.randrange(4, 9, 1)):
            address += random.choice(chars)

        line = address + '@mail.com'
        box += line + '\n'
    return box
