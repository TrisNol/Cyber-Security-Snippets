import hashlib

def dictionaryAttack(password_hash, dictionary, hash_algorithm=hashlib.md5):
    for word in dictionary:
        enc_wrd = word.encode('utf-8')
        digest = hash_algorithm(enc_wrd.strip()).hexdigest()

        if digest.strip() == password_hash.strip():
            return word
    return None


if __name__ == "__main__":
    password = "12345"
    pass_hash = hashlib.sha256(password.encode()).hexdigest()

    with open('./passwords.txt', 'r') as text:
        pw = dictionaryAttack(pass_hash, text, hash_algorithm=hashlib.sha256)
        if pw is not None:
            print('Password is: ' + pw)
        else:
            print('Password not found')