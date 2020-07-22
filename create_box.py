"""
*************
*           *
*           *
*           *
*************
"""

def boxprint(symbol,width,height):
    print(symbol * width)
    for i in range(height-2):
        print(symbol+ (' '*(width-2)*len(symbol))+symbol)
    print(symbol*width)


boxprint('-',15,6)
boxprint('*',15,6)

             
### assertion its another kind of exception
##

#######SWITCH LIGHTS#########


market={'ns':'green','ew':'red'}

def switchlights(intersection):
    for key in intersection.keys():
        if intersection[key]=='green':
            intersection[key]='yellow'
        elif intersection[key]=='yellow':
            intersection[key]='red'
        elif intersection[key]=='red':
            intersection[key]='green'

    assert 'red' in intersection.values(), 'Neither light is red!'+str(intersection)
#print(market)
print(switchlights(market))
print(market)

## assertions are sanity checks
   



