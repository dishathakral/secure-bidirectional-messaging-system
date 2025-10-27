import string, math

plain_alphabet = string.ascii_uppercase
cipher_alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"
decrypt_map = {cipher_alphabet[i]: plain_alphabet[i] for i in range(26)}

def caesar_decrypt(text, shift=3):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

def monoalphabetic_decrypt(text):
    result = ''
    for char in text:
        if char.isalpha():
            result += decrypt_map.get(char.upper(), char).lower() if char.islower() else decrypt_map.get(char, char)
        else:
            result += char
    return result
