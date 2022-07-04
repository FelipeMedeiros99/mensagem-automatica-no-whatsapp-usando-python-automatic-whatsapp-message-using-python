# processo_de_envio

def gerador_de_links(*lista_de_contatos):
    # juntando os contatos com o link
    lista_de_links = []
    for contato in lista_de_contatos:
        lista_de_links.append(link_bruto() + contato)
    return lista_de_links


def link_bruto():
    codigo_do_pais = '55'
    return "https://api.whatsapp.com/send?phone="+codigo_do_pais



def abrir_conversa(link, tempo = 0):
    import pyautogui
    import pyperclip
    from time import sleep
    # abrir chrome
    pyautogui.PAUSE = 1
    # colar o link com o contato
    pyautogui.press('win')
    if tempo >= 2.5:
        sleep(tempo - 2.5)
    pyautogui.write('google')
    sleep(tempo)
    pyautogui.press('enter')
    sleep(4)
    pyperclip.copy(link)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    sleep(2)


def fechar_navegador():
    import pyautogui
    pyautogui.hotkey('alt', 'tab')
    pyautogui.hotkey('ctrl', 'w')
