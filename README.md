### PyAutoGUI

O PyAutoGUI é uma biblioteca Python de automação de interface de usuário (UI) que permite controlar o teclado e o mouse para automatizar tarefas repetitivas em sistemas operacionais Windows, macOS e Linux. Com o PyAutoGUI, você pode escrever scripts simples para simular interações humanas, como clicar em botões, digitar texto, mover o mouse e muito mais.

#### Principais recursos:

- **Cross-Platform**: Funciona em sistemas operacionais Windows, macOS e Linux.
- **Fácil de Usar**: Oferece uma API simples e intuitiva para automatizar tarefas.
- **Suporte a Gráficos**: Permite capturar e manipular imagens da tela para interagir com aplicativos baseados em gráficos.
- **Personalizável**: Possui recursos avançados para ajustar a velocidade, intervalos de tempo e outras configurações de automação.

#### Instalação:
Para instalar o PyAutoGUI, basta executar o seguinte comando:
```python
pip install pyautogui
```
#### Exemplo de Uso:
Aqui está um exemplo simples de como usar o PyAutoGUI para clicar em um botão e digitar texto:
```python
import pyautogui
# Clica no botão "Enviar"
pyautogui.click(x=100, y=200)

# Digita "Olá, mundo!"
pyautogui.typewrite("Olá, mundo!")
```
Para mais informações e exemplos, consulte a [documentação oficial do PyAutoGUI.](https://pyautogui.readthedocs.io/en/latest/).