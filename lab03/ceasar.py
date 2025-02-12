class Caesar:
    def caesar(self):
        self._key = 0

    def get_key(self):
        return self._key

    def set_key(self, key):
        self._key = key

    def encrypt(self, plaintext):
        ciphertext = ""
        for value in plaintext:
            if value.isalpha():  
                value = value.lower()
                encrypt = chr((ord(value) - ord('a') + self._key) % 26 + ord('a'))
                ciphertext += encrypt
            elif value == " ": #add space!
                ciphertext += value
            else:
                encrypt = chr((ord(value) + self._key) % 256)
                ciphertext += encrypt
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""
        for value in ciphertext:
            if value.isalpha(): 
                value = value.lower()
                decrypt = chr((ord(value) - ord('a') - self._key) % 26 + ord('a'))
                plaintext += decrypt
            elif value == " ":
                plaintext += value
            else:
                decrypt = chr((ord(value) - self._key) % 256)
                plaintext += decrypt
        return plaintext

# example output from lab
cipher = Caesar()
cipher.set_key(3)
print(cipher.encrypt("hello WORLD!"))  # prints "khoor zruog$"
print(cipher.decrypt("KHOOR zruog$"))  # prints "hello world!"
cipher.set_key(6)
print(cipher.encrypt("zzz"))  # prints "fff"
print(cipher.decrypt("FFF"))  # prints "zzz"
cipher.set_key(-6)  # Negative keys should be supported!
print(cipher.encrypt("FFF"))  # prints "zzz"