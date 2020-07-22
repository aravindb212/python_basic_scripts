## user defined function

def simple():
    print("its a function")

simple()


def gbp_to_inr (gbp):
    inr= gbp*98
    return inr
   
inr = gbp_to_inr(1)
print(inr)
inr = gbp_to_inr(1.2)
print(inr)
inr = gbp_to_inr(2)
print(inr)

#read muntiple files using function

def printname(name):
    print (name)
printname("aravind")
printname("manu")
# cant print/read without * in function printname("aravind", "dude")


def printname(*name):
    print(name)
    print(name[1])
printname("aravind", "dude", "manu")

def printname(name,surname):
    print(name, surname)
    print(surname)
    print(name)
printname("bommalata",27)





