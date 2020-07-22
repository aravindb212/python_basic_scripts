import os
mo= os.path.join('folder1','folder2','folder3','file.jpeg')
print(mo)
print(os.sep)
print(os.getcwd())
#mo=os.chdir('c:\\')
#print(os.getcwd())

 
## .\ , ..\   ---- are relative paths
#folders in root folder are noted as  "..\"
#folders in  relative folder are noted as ".\"
#C:\........   --- are absolute paths


print(os.getcwd())
print(os.path.abspath('asjd.txt'))
print(os.path.abspath('..\\..\\asjd.txt'))
print(os.path.isabs('A:\\asjd.txt'))
print(os.path.relpath('A:\\folder1\\folder2\\asjd.txt', 'A:\\folder1'))
##slicing
print(os.path.dirname('A:\\folder1\\folder2\\asjd.txt'))
print(os.path.basename('A:\\folder1\\folder2\\asjd.txt'))


# os.path.exists(\\\path\\) --- to check whether the path really exists

# os.path.isfile() -- to check the file path

# os.path.isdir()  --- to check the folder path

#os.path.getsize() -- to check the size of a folder/file

# os.listdir('\\path\\\')  -- to see list of files/folders in directory

# 

os.makedirs('A:\\python_scripts\\nadd\\aksjd\\asda')



#####################################################

