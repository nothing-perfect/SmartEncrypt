#import required files/libs and setup varstorage
import easygui
import encrypt_func as encryptionf
import time

#import file
originalfile = easygui.fileopenbox()

#save originalfile to be used in other scripts
filewrite = open("filelocation.txt", "w")
filewrite.write((originalfile))
filewrite.close()

#launch encrypt function
encryptionf.fernet_algo()
time.sleep(13)