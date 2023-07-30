# Passo a Passo do meu projeto > Como fazer o passo a passo? > Como você resolveria esse projeto se fosse fazer manualmente
# Passo 1: Entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer Login
# Passo 3: Importar a vase de produtos para cadastrar
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o processo de cadastro até o fim

# pip install pyautogui
from time import sleep
import pyautogui  # principais comandos:
# pyautogui.write -> escrever um texto
# pag.press -> apertar 1 tecla
# pag.click -> clicar em algum lugar da tela
# pag.hotkey -> combinação de teclas
# Regra para o codigo ter um tempo em cada um dos comandos.
pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa > Usando o pyautogui
# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "shift", "n")

# entrar no link > fazendo o python simular o que uma pessoa faria usando mouse e teclado
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
sleep(3)

# Passo 2: Fazer Login


# sleep(5)
# print(pyautogui.position())

# pyautogui.scroll(200)
