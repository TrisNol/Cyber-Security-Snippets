import hashlib
import datetime
from numba import jit, njit
from itertools import product

def brute_force(characters, length, password_hash, hash_algorithm=hashlib.md5):
    for i in range(length + 1):
        for attempt in product(characters, repeat=i):
            password = ''.join(attempt)
            digest = hash_algorithm(password.encode()).hexdigest()

            if digest.strip() == password_hash.strip():
                return password
    return None

@jit(forceobj=True, parallel=True)
def brute_force_gpu(characters, length, password_hash, hash_algorithm=hashlib.md5):
    for i in range(length + 1):
        for attempt in product(characters, repeat=i):
            password = ''.join(attempt)
            digest = hash_algorithm(password.encode()).hexdigest()

            if digest.strip() == password_hash.strip():
                return password
    return None

if __name__ == "__main__":
    password = "ABC"
    pass_hash = hashlib.md5(password.encode()).hexdigest()

    start = datetime.datetime.now()
    pw = brute_force_gpu('QWERTZUIOPASDFGHJKLYXCVBNM', 5, pass_hash)
    end = datetime.datetime.now()
    if pw is not None:
        print('Password is: ' + pw)
    else:
        print('Password not found')
    print('GPU: ' + str(end - start))


    start = datetime.datetime.now()
    pw = brute_force('QWERTZUIOPASDFGHJKLYXCVBNM', 5, pass_hash)
    end = datetime.datetime.now()
    if pw is not None:
        print('Password is: ' + pw)
    else:
        print('Password not found')
    print('CPU: ' + str(end - start))