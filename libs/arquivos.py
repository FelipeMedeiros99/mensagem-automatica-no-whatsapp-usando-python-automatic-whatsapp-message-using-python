def documento():
    import os.path
    documento = os.path.join('C:\\', 'Users', 'User', 'Desktop', 'texto automatico.txt')
    documento_existe = os.path.isfile(documento)
    if documento_existe:
        ler = open(documento, 'r')
        return ler.read()

    else:
        open(documento, 'w')
        print('Documento criado na área de trabalho, digite o texto automático lá e execute novamente')
        input()


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


