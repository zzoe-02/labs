def caesar_encrypt(plaintext, key):
    ciphertext = ""
    for value in plaintext:
        if value.isalpha():
            value = value.lower()
            encrypted = chr((ord(value) - ord('a') + key) % 26 + ord('a'))
            ciphertext += encrypted
        elif value == " ":
            ciphertext += value
        else:
            encrypted = chr((ord(value) + key) % 256)
            ciphertext += encrypted
    return ciphertext


def caesar_decrypt(ciphertext, key):
   plaintext = ""
   for value in ciphertext:
        if value.isalpha():
            value = value.lower()
            decrypted = chr((ord(value) - ord('a') - key) % 26 + ord('a'))
            plaintext += decrypted
        elif value == " ":
            plaintext += value
        else:
            decrypted = chr((ord(value) - key) % 256)
            plaintext += decrypted
   return plaintext