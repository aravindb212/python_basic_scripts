def isphonenumber(text): #455-152-7541
    if len(text) !=12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False #no area code
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] !='-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
print(isphonenumber('455-147-4545'))
print(isphonenumber('heloo buddy'))


####find a number in a text

message= 'hey buddy i tried calling you please call to my number 457-545-7889 or call to my office number 889-154-5654 '
foundnumber=False
for i in range(len(message)):
    chunk=message[i:i+12]
    if isphonenumber(chunk):
        print('phone number is: '+ chunk)
        foundnumber= True
if not foundnumber:
    print('number not found')
    

#find indian phone number

def findnumber(numb):
    if len(numb)!=14:
        return False
    if numb[0]!='+':
        return False
    for i in range(1,3):
        if not numb[i].isdecimal():
            return False
    if numb[3]!= '-':
        return False
    for i in range(4,14):
        if not numb[i].isdecimal():
            return False
    return True
        
    
msge='hey man wassup u missed my call so call me back to +91-8179269412 or call to me my office number +51-5441218121 '
foundnumber=False
for i in range(len(msge)):
    chara=msge[i:i+14]
    if  findnumber(chara):
        print('the phone number is : '+ chara)
        foundnumber=True
if not foundnumber:
    print('number not found')
        
##### using regula expression find indian number

import re
msge='hey man wassup u missed my call so call me back to +92-8179269412 or call to me my office number +61-5441218121 '
phonenumregex=re.compile( r'(\+\d\d)\-(\d\d\d\d\d\d\d\d\d\d)')
mm=phonenumregex.search(msge)
nm1=phonenumregex.findall(msge)
print('number found: '+ mm.group())
print('numbers found in the msg: '+ str(nm1))
print('code ' +mm.group(1)+ 'number'+ mm.group(2) )
print(nm1)

## using pipe character |

batregex=re.compile(r'Aravi(_nano|imMr.A|B|Bommarillu)')
me=batregex.search('aravind has social media accounts with name Aravi_nano')
print(me.group())
mo=batregex.search('aravind has social media accounts with name Aravindb212')
print(mo)


