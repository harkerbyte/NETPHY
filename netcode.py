import os 
import tokenize 
import sys 

if sys.version_info[0] !=3:
    print('please do install python3')

from ast import Try, Break 
from urllib import request
print('(⓿_⓿) i can help you get a web page source code (‾◡◝)')

Break
url =input('paste web page link here:')

print('\033[2;43m (⌐■_■) compiling codes for better view \033[0;0m')

Break

x = url 
request.post(url)
print(x.content)
