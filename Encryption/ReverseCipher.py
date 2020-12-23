
class ReverseCipher():

    def encrypt(self, text):
        message = ""
        i = len(text) - 1
        while i >= 0:
            message += text[i]
            i = i - 1
        return message

    def decrypt(self, text):
        return self.encrypt(text)


if __name__ == "__main__":
    cipher = ReverseCipher()
    text = "This is reverse cipher"

    enc = cipher.encrypt(text)
    print(enc)
    print(cipher.decrypt(enc))