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
import  urllib.request
import re
def getHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    print('get html')
    return str(html)

def getImg(html):
    reg=r'"BDE_Image" src="(.*?\.jpg)" pic_ext'
    imgre=re.compile(reg)
    imglist=re.findall(reg,html)
    print(len(imglist))
    x=0
    for img in imglist:
##        urllib.request.urlretrieve(img,'hjj%s.jpg'%x)
        print(img)
        x+=1
    else:
        print('ok')

if __name__ == '__main__':
    html=getHtml("http://tieba.baidu.com/p/2476135832?pn=2")
    getImg(html)
