import shutil
mo=shutil.copy('A:\\new.txt', 'A:\\python_scripts')
#
mo=shutil.copy('A:\\new.txt', 'A:\\python_scripts\\newnewe.txt')

#shutil.copytree('A:\\python_scripts', 'A:\\python_scripts_backup')
#shutil.move('A:\\new.txt','A:\\python_scripts')
#we can also move file or folder in the same folder with differnet name



### deleting files

import os
print(os.getcwd())
os.unlink('new.txt')
os.rmdir('c:\\folder1\folder2')#emptyfolder
shutil.rmtree('c:\\folder1\folder2')#delete folder permanently


#os.chdir('dasdasas') ## change current directory
#for filename in os.listdir():
    # if filename.endswith('.txt'):
        #print(filename)
         #os.unlink(filename)

## INSTEAD of deleting permentaly we send files to trash
    #using send2trash


    #install send2trash to use

    #import send2trash
    #send2trash.send2trash('asdjasldas/skdjalsjds')
     
