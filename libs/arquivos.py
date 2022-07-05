def documento():
    import os.path
    documento = os.path.join('C:\\', 'Users', 'User', 'Desktop', 'texto automatico.txt')
    documento_existe = os.path.isfile(documento)

    if documento_existe:
        with open(documento, 'r', encoding='utf-8') as ler:
            return ler.read()
    else:
        with open(documento, 'w'):
            print('Documento criado na área de trabalho, digite o texto automático lá e execute novamente')


def busca_texto_e_envia():
    import pyautogui
    import pyperclip
    pyautogui.PAUSE = 1
    pyperclip.copy(documento())
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')


def lista_de_contatos():
    import os.path
    contatos = os.path.join('C:\\', 'Users', 'User', 'Desktop', 'contatos.txt')
    lista_existe = os.path.isfile(contatos)
    if lista_existe:
        ler_contatos = open(contatos, 'r')

        lista = set(contatos for contatos in ler_contatos.read().split('\n'))
        return lista
    else:
        open(contatos, 'w+')
        print('documento "contatos" criado na área de trabalho, adicione os contatos e execute novamente.')
        input()


def pasta_de_arquivos():
    import os

    pasta = os.path.join('C:\\', 'Users', 'User', 'Desktop', 'arquivos_para_envio_wpp')
    existe_pasta = os.path.isfile(pasta)

    pasta_fotos = os.path.join('C:\\', 'Users', 'User', 'Desktop', 'arquivos_para_envio_wpp', 'fotos')
    existe_pasta_fotos = os.path.exists(pasta_fotos)

    pasta_documentos = os.path.join('C:\\', 'Users', 'User', 'Desktop', 'arquivos_para_envio_wpp', 'documentos')
    existe_pasta_documentos = os.path.exists(pasta_documentos)

    if not existe_pasta:
        os.makedirs(pasta)
        print('Pasta de arquivos com o nome "arquivos_para_envio_wpp" criada na área de trabalho, '
              'adicione os arquivos para enviar lá')

    if not existe_pasta_fotos:
        os.makedirs(pasta_fotos)

    if not existe_pasta_documentos:
        os.makedirs(pasta_documentos)


def tab_invertido():
    from pyautogui import keyUp, keyDown, press

    keyDown('shift')
    press('tab')
    keyUp('shift')


def envia_fotos():
    from pyautogui import press, hotkey
    from time import sleep
    import pyperclip

    sleep(4)
    # ETAPA 1, ABRIR EXPLORADOR DE ARQUIVOS

    # abrir o anexar do whatsapp clicando shift + tab
    tab_invertido()
    # pressionar enter
    press('enter')
    sleep(1)
    # abrir fotos e videos clicando na seta pra baixo
    press('down')
    sleep(0.5)
    # pressionar enter
    press('enter')
    sleep(1)

    # ETAPA 2, BUSCAR ARQUIVO
    # copiando diretório
    pyperclip.copy(r'C:\Users\User\Desktop\arquivos_para_envio_wpp\fotos')
    # barra de pesquisa ctrl + f
    hotkey('ctrl', 'f')
    sleep(1)
    # barra de endereços shift tab
    tab_invertido()
    sleep(1)
    # enter
    press('enter')
    sleep(1)
    # colar diretório
    hotkey('ctrl', 'v')
    sleep(1)
    # enter
    press('enter')
    sleep(1)
    # ir para as imagens
    hotkey('crtl','f')
    sleep(1)
    press('tab', presses=3)
    sleep(1)
    # selecionar tudo ctrl + a
    hotkey('ctrl', 'a')
    sleep(1)
    # enter
    press('enter')
    # esperar um pouco
    sleep(3)
    # enter
    press('enter')


def envia_documentos():
    from pyautogui import press, hotkey, write
    from time import sleep
    import pyperclip


    sleep(4)
    # ETAPA 1, ABRIR EXPLORADOR DE ARQUIVOS

    # abrir o anexar do whatsapp clicando shift + tab
    tab_invertido()
    # pressionar enter
    press('enter')
    sleep(1)
    # abrir fotos e videos clicando na seta pra baixo
    press('down')
    sleep(0.5)
    # pressionar enter
    press('enter')
    sleep(1)

    # ETAPA 2, BUSCAR ARQUIVO
    # copiando diretório
    pyperclip.copy(r'C:\Users\User\Desktop\arquivos_para_envio_wpp\documentos')
    # barra de pesquisa ctrl + f
    hotkey('ctrl', 'f')
    sleep(1)
    # barra de endereços shift tab
    tab_invertido()
    sleep(1)
    # enter
    press('enter')
    sleep(1)

    # colar diretório
    hotkey('ctrl', 'v')
    sleep(1)
    # enter
    press('enter')
    sleep(1)

    # all files
    hotkey('ctrl', 'f')
    for c in range(6):
        press('tab')
        sleep(0.5)

    write('a')

    # ir para os documentos
    hotkey('ctrl', 'f')
    sleep(1)
    press('tab')
    sleep(0.5)
    press('tab')
    sleep(0.5)
    press('tab')
    sleep(0.5)

    # selecionar tudo ctrl + a
    hotkey('ctrl', 'a')
    sleep(1)
    # enter
    press('enter')
    # esperar um pouco
    sleep(3)
    # enter
    press('enter')







