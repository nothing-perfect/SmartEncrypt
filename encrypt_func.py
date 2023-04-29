import cryptography

def fernet_algo():
    #encryption algorithm 1 aka fernet
    #key generation
    key = Fernet.generate_key()
 
    #string the key in a 
    try:
        with open('key', 'wb') as filekey:
            filekey.write(key)
            filekey.close()
            filekey.flush
    except:
        print ("error")
   
    # opening the key
    with open('key', 'rb') as filekey:
        key = filekey.read()
 
    # using the generated key
    fernet = Fernet(key)
 
    # opening the original file to encrypt
    with open((originalfile), 'rb') as file:
        original = file.read()
     
    # encrypting the file
    encrypted = fernet.encrypt(original)
 
    # opening the file in write mode and
    # writing the encrypted data
    with open('encrypted.txt', 'wb') as encfile:
        encfile.write(encrypted)
        encfile.flush()
        encfile.close()