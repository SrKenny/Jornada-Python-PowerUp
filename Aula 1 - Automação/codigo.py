# Passo 1: Entra no sistema https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Passo 2: Fazer Login
# Passo 3: Importar a base de dados
# Passo 4: Cadastra produto
# Passo 5 : Repetir o processo de cadastro até acabar os produtos  
import pyautogui
import pandas as pd
import time

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# pyautogui.write -> escreve um texto
# pyautogui.click -> clicar com o mouse
# pyautogui.press -> pressionar uma tecla
# pyautogui.hotkey -> aperta atalhos de teclado (Ctrl, C)

pyautogui.PAUSE = 0.5
# abrindo o sistema
pyautogui.press("win")
pyautogui.write("brave") # Qualquer navegador 
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)


pyautogui.click(x=550, y=400) # valores (x,y) dependem da resolução do monitor
pyautogui.write("emaildeteste@gmail.com")
pyautogui.press("tab")
pyautogui.write("qualquersenha")
pyautogui.click(x=700, y=570)

time.sleep(2)


tabela = pd.read_csv("Aula 1 - Automação\produtos.csv")


for linha in tabela.index:
    
    pyautogui.click(x=432, y=287)
    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    # preco
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    # observação
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.press("home")


