import pyautogui
from time import sleep
'''
Funções:
    pyautogui.click() - Clica em algum lugar da tela
    pyautogui.write() - Escreve um texto
    pyautogui.press() - Pressiona alguma tecla do teclado
'''

# Abrir o windows
pyautogui.press("win")
# Digita o navegador de acordo com que o pc tem instalado
pyautogui.write("Brave");sleep(2)
# Abre o navegador
pyautogui.press("enter")