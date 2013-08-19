#-------------------------------------------------------------------------------
# Name:        妯″潡1
# Purpose:
#
# Author:      HJJ
#
# Created:     15/08/2013
# Copyright:   (c) HJJ 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import re
r=r'a[oi]p'
result0=re.match(r,'aop aip asp ai')
print(result0.group(0))

result1=re.search(r,'aop aip asp ai')
print(result1)

r1=re.compile(r,re.I)
print(r1.findall('aop aip asp Ai'))

rs=r'c..t'
print(re.sub(rs,'python','csvt caat sd'))

s='''
    hello csvt
    csvt
    asdasd
    csvt
    '''
print(re.findall(rs,s,re.M))