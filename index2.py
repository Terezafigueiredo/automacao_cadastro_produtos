import time
import pyautogui
import pandas

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True  # mover o mouse para o canto superior esquerdo interrompe

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

try:
    # Passo 1: Entrar no sistema da empresa
    pyautogui.press("win")
    pyautogui.write("edge")
    pyautogui.press("enter")
    time.sleep(2)

    pyautogui.hotkey("ctrl", "l")
    pyautogui.write(link, interval=0.05)
    pyautogui.press("enter")

    # Passo 2: Fazer login (novas coordenadas)
    pyautogui.click(x=698, y=405)
    pyautogui.write("pythonimpressionador@gmail.com")
    pyautogui.press("tab")
    pyautogui.write("sua senha")
    pyautogui.click(x=938, y=565)
    time.sleep(3)

    # Passo 3: Abrir a base de dados (importar o arquivo)
    tabela = pandas.read_csv('produtos.csv')
    tabela = tabela.drop_duplicates(subset='codigo')  # evita cadastrar duplicados
    print(tabela)

    # Passo 4: Cadastrar produtos (novas coordenadas)
    for linha in tabela.index:
        # código
        pyautogui.click(x=701, y=282)
        codigo = str(tabela.loc[linha, 'codigo'])
        pyautogui.write(codigo)
        pyautogui.press('tab')

        # marca
        marca = str(tabela.loc[linha, 'marca'])
        pyautogui.write(marca)
        pyautogui.press('tab')

        # tipo
        tipo = str(tabela.loc[linha, 'tipo'])
        pyautogui.write(tipo)
        pyautogui.press('tab')

        # categoria
        categoria = str(tabela.loc[linha, 'categoria'])
        pyautogui.write(categoria)
        pyautogui.press('tab')

        # preço
        preco = str(tabela.loc[linha, 'preco_unitario'])
        pyautogui.write(preco)
        pyautogui.press('tab')

        # custo
        custo = str(tabela.loc[linha, 'custo'])
        pyautogui.write(custo)
        pyautogui.press('tab')

        # observação
        obs = str(tabela.loc[linha, 'obs'])
        if obs != 'nan':
            pyautogui.write(obs)
        pyautogui.press('tab')
        pyautogui.press('enter')

        # voltar para o início da tela
        pyautogui.scroll(5000)

except pyautogui.FailSafeException:
    print("⚠️ Automação interrompida manualmente! Mouse levado ao canto superior esquerdo da tela.")
