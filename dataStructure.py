shoplist=['mango','banana','apple']
for i in shoplist:
    print(i,end=',')
shoplist.append('rice')
shoplist.sort()
print(shoplist)
del shoplist[0]
print(shoplist)

zoo=('wolf','elephant','penguin')
new_zoo=('monkey','dolphin',zoo)
print('%s is last'%new_zoo[2][2])

ab={'tom':'tom1','jerry':'jerry1','lily':'lily1'}
ab['tom']='tom2'
ab['larry']='larry1';
del ab['jerry']
for k,v in ab.items():
    print('key is %s,value is %s'%(k,v))

if 'tom' in ab or ab.has_key('tom'):
    print('has!')

name='swaroop'
print(name[1:3])

if name.startswith('swa'):
    print('swa')
if 'a' in name:
    print('a')
if name.find('oop')!=-1:
    print('oop')
limiter='_'
list0=['a','b','c']
print(limiter.join(list0))
