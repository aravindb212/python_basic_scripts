#cat={'name':'bunny','age':'6','color':'black'}
#allcat=[]
#allcat.append({'name':'bunny','age':'6','color':'black'})
#allcat.append({'name':'sophie','age':'8','color':'gray'})

#allcat.append({'name':'large','age':'7','color':'black'})

#allcat.append({'name':'????','age':'6','color':'orange'})
#print(allcat)


#### tic tac toe sample

import pprint
theboard={'top-L':'X','top-M':'','top-R':'',
          'mid-L':'','mid-M':'','mid-R':'',
          'low-L':'','low-M':'','low-R':''}
print(theboard)
pprint.pprint(theboard)
theboard['top-L']=''

pprint.pprint(theboard)
theboard['top-L']='0'
theboard['top-M']='X'
theboard['top-R']='X'
theboard['low-R']='0'
theboard['low-L']='X'
theboard['mid-M']='0'
theboard['mid-L']='0'
theboard['mid-R']='0'
theboard['low-M']='X'
pprint.pprint(theboard)

def printboard(board):
    print(board['top-L']+ '|'+board['top-M']+'|'+board['top-R'])
    print('-----')
    print(board['mid-L']+ '|'+board['mid-M']+'|'+board['mid-R'])
    print('-----')
    print(board['low-L']+ '|'+board['low-M']+'|'+board['low-R'])
printboard(theboard)
