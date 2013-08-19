poem='''11111111
22222222
3333333
'''
f=open(r'e:\MyTest\PythonDemo\poem.txt','w')
f.write(poem)
f.close()

f=open(r'e:\MyTest\PythonDemo\poem.txt')
while True:
    line=f.readline()
    if len(line)==0:
        break
    print(line,end='')
f.close()


import pickle as p
shoplistfile='e:\MyTest\PythonDemo\shoplist.data'
shoplist=['apple','mango','carrot']
f=open(shoplistfile,'wb')
p.dump(shoplist,f)
f.close()

f=open(shoplistfile,'rb')
storedlist=p.load(f)
print(storedlist)
