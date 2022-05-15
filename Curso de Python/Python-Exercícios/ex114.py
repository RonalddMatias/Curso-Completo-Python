import urllib
import urllib.request 
import pyautogui

pyautogui.write
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site não está acessível no momento!')
else:
    print('O site está acessível!')
    print(site.read()) #O read vai informar no terminal todo o codigo do site pudim.