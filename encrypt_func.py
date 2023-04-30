#import required libs/files
from cryptography.fernet import Fernet
import time
import os
import subprocess
import sys
import main

#get file location
file = open("filelocation.txt", "r")
originalfile = file.read()
file.close()

def fernet_algo():

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
    with open((originalfile),'rb') as file:
        original = file.read()
     
    # encrypting the file
    encrypted = fernetkey.encrypt(original)
 
    # opening the file in write mode and writing the encrypted data
    try:
        with open((originalfile),'wb') as encfile:
            encfile.write(encrypted)
            print ("writing encrypted file...")
            time.sleep(4)
            encfile.flush()
    except:
        print ("error writing 'encrypted.txt'.  Does SmartEncrypt have permision to write files here?")
    
    #restart main script
    print ("would you like to encrypt or decrypt another file? Y or N")
    choice = input()
    if choice == "Y":
        # Run the other script
        main.main
    elif choice == "N":
        print ("Goodbye.")
        time.sleep(3)
        sys.exit()
    