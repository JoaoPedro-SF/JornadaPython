# Passo a Passo do meu projeto > Como fazer o passo a passo? > Como você resolveria esse projeto se fosse fazer manualmente
# Passo 1: Entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer Login
# Passo 3: Importar a vase de produtos para cadastrar
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o processo de cadastro até o fim

# pip install pyautogui
import pandas as pd
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
# selecionar o campo de email
pyautogui.click(x=2712, y=392)
# escrever o email/senha
pyautogui.write("Teste@gmail.com")
pyautogui.press("tab")  # passando para proximo campo
pyautogui.write("teste1")
pyautogui.click(x=2878, y=555)  # click botão login
sleep(3)

# Passo 3: Importar a vase de produtos para cadastrar
# pip install pandas

tabela = pd.read_csv("produto.csv")
print(tabela)
# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código -> x=2716, y=278
    pyautogui.click(x=2716, y=278)

    # pegar da tabela o valor do campo que a gente quer preencher
    # esolhendo um item na tabela usando o .loc
    codigo = tabela.loc[linha, "codigo"]

    # prencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")  # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
