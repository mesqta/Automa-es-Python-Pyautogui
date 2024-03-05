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
pyautogui.write("Brave");sleep(1)
# Abre o navegador
pyautogui.press("enter");sleep(1)
# Coloca o site no campo de busca
link = "https://github.com/mesqta"
# Coloca o link no campo de pesquisa
pyautogui.write(link);sleep(2)
pyautogui.press("enter");sleep(1)


'''
    função sleep:
        a função sleep  é usada para dar uma pausa na execução do programa por um tempo determinado,
        permitindo assim que outras operações sejam executadas enquanto ele está dormindo.

'''