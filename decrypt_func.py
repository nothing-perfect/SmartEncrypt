#import required libs/files
from cryptography.fernet import Fernet
import time
import os
import base64

def fernet_algo():   

    file = open("filelocation.txt", "r")
    originalfile = file.read()
    file.close()


    # using the key
    print("type in the key from smartencrypt.key.txt")
    key = input()
    fernet = Fernet(key)
 
    # opening the encrypted file
    with open((originalfile), 'rb') as enc_file:
        encrypted = enc_file.read()
 
    # decrypting the file
    decrypted = fernet.decrypt(encrypted)
 
    # opening the file in write mode and
    # writing the decrypted data
    try:
        with open((originalfile), 'wb') as dec_file:
            dec_file.write(decrypted)
            print ("Succesfully wrote encrypted file.")
    except:
     print ("ran into a problem writing decrypted file")