import os
command='"c:\\Program Files\\WinRAR\\Rar.exe" a -k -r -s -m1 d:\\web.rar d:\\web\\'
print(command)
os.system(command)
