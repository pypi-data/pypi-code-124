import random
import string


def random_id(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
