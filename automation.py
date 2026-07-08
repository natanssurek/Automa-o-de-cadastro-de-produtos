#Importando as bibliotecas necessárias para fazer a automação
import pyautogui
import time 
import pandas

#Passo 1: Abrir o windows
#Passo 2: Entrar no navegador
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("Enter")

#Passo 3: Entrar no link do sistema 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("Enter")
time.sleep(5)

#Passo 4: Fazer login
pyautogui.click(x=907, y=497)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("Tab")
pyautogui.write("sua senha muito muito dificilima") 
#Passo 5: Cadastrar 1 produto 
#Passo 6: Repetir o passo 5 até acabar os produtos que precisam ser registrados



