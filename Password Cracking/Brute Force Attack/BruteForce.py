import hashlib
from itertools import product

def brute_force(characters, length, password_hash):
    for i in range(length + 1):
        for attempt in product(characters, repeat=i):
            password = ''.join(attempt)
            digest = hashlib.md5(password.encode()).hexdigest()

            if digest.strip() == password_hash.strip():
                return password
    return None

if __name__ == "__main__":
    password = "HELLO"
    pass_hash = hashlib.md5(password.encode()).hexdigest()

    pw = brute_force('QWERTZUIOPASDFGHJKLYXCVBNM', 5, pass_hash)
    if pw is not None:
        print('Password is: ' + pw)
    else:
        print('Password not found')