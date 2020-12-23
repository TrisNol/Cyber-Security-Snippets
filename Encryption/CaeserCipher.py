
class CaesarCipher():

    def encrypt(self, text, s):
        result = ""

        for i in range(len(text)):
            char = text[i]

            if (char.isupper()):
                result += chr((ord(char) + s - 65) % 26 + 65)
            
            elif (char == ' '):
                result += char

            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        return result

    def decrypt(self, text, s):
        result = ""

        for i in range(len(text)):
            char = text[i]

            
            if (char.isupper()):
                result += chr((ord(char) - s - 65) % 26 + 65)

            elif (char == ' '):
                result += char

            else:
                result += chr((ord(char) - s - 97) % 26 + 97)
        return result

    def detectShift(self, text):
        hashMap = {}
        for char in text:
            if(char in hashMap):
                hashMap[char] += 1
            else:
                hashMap[char] = 1
        maxCount = 0
        maxCharacter = None
        for key in hashMap:
            if(hashMap[key] > maxCount):
                maxCharacter = key
                maxCount = hashMap[key]
        return (ord(maxCharacter.upper()) - ord('E'))


if __name__ == "__main__":
    cipher = CaesarCipher()
    text = "Caesar Cipher Demo"
    s = 4

    encrypted = cipher.encrypt(text, s)
    decrypted = cipher.decrypt(encrypted, s)
    print ("Plain Text : " + text)
    print ("Shift pattern : " + str(s))
    print ("Cipher: " + encrypted)

    print("Decrypt: " + decrypted)
    print(cipher.decrypt(encrypted, cipher.detectShift(encrypted)))