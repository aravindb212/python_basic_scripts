mycat={'size':'fat','color':'gray','disposition':'loud'}
mycat['size']


##
[1,2,3]==[3,2,1]
#output is false

#but in dictionaries its different

mycats={'disposition':'loud','color':'gray','size':'fat'}
mycat==mycats #its results true


'name' in mycat

x=list(mycat.values())
print(x)

x=list(mycat.items())
print(x)

x=mycat.keys()
print(x)


for items in mycat.keys():
    print(items)
for items in mycat.values():
    print(items)
for items in mycat.items():
    print(items)
for k,v in mycat.items():
    print(k,v)

if 'species' in mycat:
    print(mycat['species'])
    
x=mycat.get('size',0)
print(x)
x=mycat.get('species','0 ')
print(x)
