# Importando as bibliotecas necessárias para fazer a automação
import pyautogui
import time
import pandas

# Passo 1: Abrir o windows
# Passo 2: Entrar no navegador
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("Enter")

# Passo 3: Entrar no link do sistema
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("Enter")
time.sleep(5)

# Passo 4: Fazer login
pyautogui.click(x=907, y=497)
pyautogui.write("administrador@gmail.com")
pyautogui.press("Tab")
pyautogui.write("SenhaDoADM12345")
pyautogui.press("Tab")
pyautogui.press("Enter")

# Abrindo a base de dados
infoTabela = pandas.read_csv("produtos.csv")
# print (infoTabela)

# Passo 5: Cadastrar 1 produto
for linha in infoTabela.index:
    # Código
    pyautogui.click(x=905, y=373)
    codigo = str(infoTabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("Tab")
    # Marca
    marca = str(infoTabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("Tab")
    # Tipo
    tipo = str(infoTabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("Tab")
    # Categoria
    categoria = str(infoTabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("Tab")
    # Preço Unitário
    precoUni = str(infoTabela.loc[linha, "preco_unitario"])
    pyautogui.write(precoUni)
    pyautogui.press("Tab")
    # Custo
    custo = str(infoTabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("Tab")
    # Obs
    obs = str(infoTabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("Tab")

    pyautogui.press("Enter")
    pyautogui.scroll(5000)

