#import required files/libs and setup varstorage
import easygui
import encrypt_func as encryptionf
import decrypt_func as decryptionf
import time
import base64

#print info
print ("SmartEncrypt 2023 nothingperfectsoft. This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to redistribute it under certain conditions")
time.sleep(5)

#import file
print ("choose a file to encrypt OR decrypt")
time.sleep(2)
originalfile = easygui.fileopenbox()

#save originalfile to be used in other scripts
filewrite = open("filelocation.txt", "w")
filewrite.write((originalfile))
filewrite.close()

print ("encrypt or decrypt?(1 or 2)")
cryptc = eval(input())

if cryptc == 1:
    #launch encrypt function
    encryptionf.fernet_algo()
    time.sleep(3)
    
else:
    #launch decrypt function
    decryptionf.fernet_algo()
    time.sleep(3)