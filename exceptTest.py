import sys
try:
    s=input('enter something:')
    raise Exception     
except EOFError:
    print('none')
except:
    print('error')
finally:
    print('finally')
