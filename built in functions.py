#import random, os, math, sys
#print(random.randint(1,10))

#print('Heyyyy! ')
#sys.exit()
#print('byeeee! ')



##### create functions

def hello():
    print('Hey buddy')
    print("dude wass up ")

hello()
hello()
hello()
hello()

########

def hello(name):
    print("hii i am "+ name )

hello('asdase')
hello('aravind')


#######
def spam():
    #global eggs
    eggs='hiii !'
    print(eggs)
    
eggs= 34
spam()
print(eggs)

##### try and except

def div2by(divideBY):
    try:
        return 42/ divideBY
    except ZeroDivisionError:
        print('Error: you try to divide by zero')
#   except NameError:
#    return     print('Error: you have used a name instead of number')
print(div2by(2))
print(div2by(12))
print(div2by(0))
print(div2by(5))
#print(div2by(Sd))
