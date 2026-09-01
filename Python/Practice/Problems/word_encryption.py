import string
import random 

#Encrypt
chars = list(" " + string.punctuation + string.ascii_letters + string.digits)
key = chars.copy()
random.shuffle(key)

secret_word = input("Original word : ") 
ciphered_word = ""

for char in secret_word:
    ciphered_word += key[chars.index(char)]

print(f"Original Text  : {secret_word}")
print(f"Encrypted Text : {ciphered_word}")

#Decrypt
decrypt_word = input("Encrypted word : ")
original_word = ""

for char in decrypt_word:
    original_word += chars[key.index(char)]

print(f"Encrypted Text : {decrypt_word}")
print(f"Original Text  : {original_word}")