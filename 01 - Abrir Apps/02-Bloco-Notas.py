import pyautogui
from time import sleep

'''
Funções:
    pyautogui.click() - Clica em algum lugar da tela
    pyautogui.write() - Escreve um texto
    pyautogui.press() - Pressiona alguma tecla do teclado
'''

pyautogui.press("win")
pyautogui.write("notepad");sleep(1)
pyautogui.press("enter")

# Escrveer algo no bloco de notas
pyautogui.write("Olá, Mundo!")
