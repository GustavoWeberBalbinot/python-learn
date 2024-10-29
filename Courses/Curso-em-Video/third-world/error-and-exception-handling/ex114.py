#Crie um programa que verifique se o site está acessível no momento ou não

import webbrowser

try:
    webbrowser.open("https://pudim.com.br")
    print('It worked')
except(webbrowser.Error):
    print('It didnt work')
