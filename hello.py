number=23
while False:
    guess=int(input('input a int:'))
    if guess!=0:
        if guess==number:
            print('=')
        elif guess<number:
            print('<')
        else:
            print('>')
    else:
        break
    
for i in range(1,5):
    print(i)
    
def Sayhello(str):
    print(str+' say hello!')
Sayhello('tom')
def GetMax(x,y):
    '''Get Max Number

    return Max'''
    if x>=y:
        return x
    else:
        return y
z=GetMax(4,5)
print(z)
print(GetMax.__doc__)
