import pyautogui 
import time
import pandas

#Atalho de abrir busca e navegador
pyautogui.keyDown('command')
pyautogui.press('space')
pyautogui.keyUp('command')
pyautogui.write('firefox')
pyautogui.press('return')

#Link do site
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
time.sleep(0.3)
pyautogui.press('return')
time.sleep(0.3)
pyautogui.press('tab')

#login
pyautogui.write('kaio.dias')
time.sleep(0.3)
pyautogui.press('tab')
pyautogui.write('Teste123')
pyautogui.press('tab')
pyautogui.press('return')
time.sleep(0.3)
pyautogui.press('tab')
time.sleep(0.3)

#importa lista de produtos.csv
tabela = pandas.read_csv('produtos.csv')
print(tabela)

#Percorre as linhas da tabela, preenchendo cada campo com a sua respectiva coluna
for linha in tabela.index:

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    time.sleep(0.3)
    pyautogui.press('tab')


    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    time.sleep(0.3)
    pyautogui.press('tab')


    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    time.sleep(0.3)
    pyautogui.press('tab')


    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    time.sleep(0.3)
    pyautogui.press('tab')


    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    time.sleep(0.3)
    pyautogui.press('tab')


    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    time.sleep(0.3)
    pyautogui.press('tab')


    obs = tabela.loc[linha, "obs"]
    #Condição pra caso o campo obs não tenha registro na coluna da linha listada, não inserir nenhum registro
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('tab')
    pyautogui.press('return')

    #Gambiarra pra retornar até o primeiro registro do formulário
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')





#time.sleep(5)
#print(pyautogui.position())

#pyautogui.press('return')
#pyautogui.scroll(5000)
