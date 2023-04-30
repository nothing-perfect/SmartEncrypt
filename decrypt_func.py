#import required libs/files
from cryptography.fernet import Fernet
import time
import os
import base64

def decrypt_fernet(): 
  
    #get the file to decrypt
    file = open("filelocation.txt", "r")
    originalfile = file.read()
    file.close()


    # getting the key
    print("type in the key from smartencrypt.key.txt which resides in the program directory")
    key = input()
    fernet = Fernet(key)
 
    # opening the encrypted file
    with open((originalfile), 'rb') as enc_file:
        encrypted = enc_file.read()
 
    # decrypting the file
    try:
        decrypted = fernet.decrypt(encrypted)
    except:
        print ("Key is incorrect")
 
    # opening the file in write mode and writing the decrypted data
    try:
        with open((originalfile), 'wb') as dec_file:
            dec_file.write(decrypted)
            print ("writing decrypted file...")
            print ("Succesfully wrote decrypted file.")
    except:
     print ("ran into a problem writing decrypted file")
    