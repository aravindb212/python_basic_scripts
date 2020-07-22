#class and objects

class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b


#class and methods

class class1:
    var1= "i'm class 1st"
class class2:
    var2= "i'm class 2nd"
class class3(class1, class2):
    var3= "i'm class 3rd"

printx = class3()

x=printx.var1
print(x)
x=printx.var2
print(x)
x=printx.var3
print(x)


## write and read a file

file= open('A:/python_scripts/file.txt','w')
file.write("hey buddy paste it")
file.close()
file= open('A:/python_scripts/file.txt','r')
file.read(11)
file.read()
