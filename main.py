#import required files/libs and setup varstorage
import easygui
import encrypt_func

#import file
originalfile = easygui.fileopenbox()

#launch encrypt function
encrypt_func.fernet_algo