from cryptography.fernet import Fernet
import time
import os

#open text file in read mode
file = open("filelocation.txt", "r")
originalfile = file.read()
file.close()

def fernet_algo():
    #encryption algorithm 1 aka fernet
    
    #generating the key
    key = Fernet.generate_key()
 
    #writing the key to a file named 'smartencrypt.key'
    try:
        with open('smartencrypt.key.txt', 'wb') as filekey:
            filekey.write(key)
            print ("writing key file...")
            time.sleep(4)
            filekey.close()
    except:
        print ("Error creating 'smartencrypt.key.txt'. Does SmartEncrypt have permision to write files here?")
   
    # opening the key
    with open('smartencrypt.key.txt','rb') as filekey:
        key = filekey.read()
 
    # using the generated key
    fernetkey = Fernet(key)
 
    # opening the original file to encrypt
    with open((originalfile), 'rb') as file:
        original = file.read()
     
    # encrypting the file
    encrypted = fernetkey.encrypt(original)
 
    # opening the file in write mode and
    # writing the encrypted data
    try:
        with open((originalfile), 'wb') as encfile:
            encfile.write(encrypted)
            print ("writing encrypted file...")
            time.sleep(4)
            encfile.flush()
    except:
        print ("error writing 'encrypted.txt'.  Does SmartEncrypt have permision to write files here?")