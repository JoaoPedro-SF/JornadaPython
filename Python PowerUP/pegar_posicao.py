from time import sleep
import pyautogui
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

sleep(5)
print(pyautogui.position())
# Point(x=2712, y=392)   posição email
# posição do logar Point(x=2878, y=555)
# posição do primeiro código produto Point(x=2716, y=278)
pyautogui.scroll(200)
