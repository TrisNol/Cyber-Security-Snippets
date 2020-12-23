import hashlib

def dictionaryAttack(password_hash, dictionary):
    for word in dictionary:
        enc_wrd = word.encode('utf-8')
        digest = hashlib.md5(enc_wrd.strip()).hexdigest()

        if digest.strip() == password_hash.strip():
            return word
    return None


if __name__ == "__main__":
    password = "12345"
    pass_hash = hashlib.md5(password.encode()).hexdigest()

    pw = dictionaryAttack(pass_hash, open('./passwords.txt', 'r'))
    if pw is not None:
        print('Password is: ' + pw)
    else:
        print('Password not found')