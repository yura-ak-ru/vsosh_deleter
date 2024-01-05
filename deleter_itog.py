# import pip
# pip.main(['install','cryptography'])
import cryptography
import os
from cryptography.fernet import Fernet
cipher_key = Fernet.generate_key()
# print(cipher_key)
cipher = Fernet(cipher_key)
print('''
  _   _       _           _           _                  
 | | | |   __| |   __ _  | |   __ _  | |_    ___    _ __ 
 | | | |  / _` |  / _` | | |  / _` | | __|  / _ \  | '__|
 | |_| | | (_| | | (_| | | | | (_| | | |_  | (_) | | |   
  \___/   \__,_|  \__,_| |_|  \__,_|  \__|  \___/  |_|   
                    by Юрий Кашников
''')
print('Скрипт для безвозвратного удаления данных с использованием шифрования')
print('Для использования скрипта запустите его из каталога с файлами, которые требуется удалить')
print('Рабочий каталог:', os.getcwd())
print('ВНИМАНИЕ! В СЛУЧАЕ ПРОДОЛЖЕНИЯ ВСЕ ФАЙЛЫ В КАТАЛОГЕ', (os.getcwd()).upper(), 'БУДУТ БЕЗВОЗВРАТНО УДАЛЕНЫ!')
choice = input('Вы уверены, что хотите продолжить? (Да/Нет)')
counter = 0
if choice == 'Да':
    for filename in os.listdir():
        if os.path.isfile(filename) and filename != 'deleter.py':
            os.rename(filename, 'deleted.txt')
            file = open("deleted.txt", "rb+")
            text = file.read()
            encrypted_text = cipher.encrypt(text)
            # print(encrypted_text)
            decrypted_text = cipher.decrypt(encrypted_text)
            file.seek(0)
            file.write(encrypted_text)
    # print(decrypted_text)
            file.close()
            os.remove('deleted.txt')
            print('Файл', filename, 'удалён')
            counter += 1
    print('Работа программы завершена. Было удалено', counter, 'файлов')
    input('Нажмите ENTER для выхода')
else:
    input('Операция отменена. Нажмите ENTER для выхода')
    exit()
# file1 = open('decrypted_tux.txt', "rb+")
# file1.seek(0)
# file1.write(decrypted_text)
# file1.close()
