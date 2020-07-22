print('my count: ')
for i in range(6):
    if i==2:
        continue
    print('count number '+ str(i))
    
    
#########

total= 0
for i in range(101):
    print(str(total)+' + ' + str(i) + ' total is :'+str(total))
    total+=i
print(total)    
