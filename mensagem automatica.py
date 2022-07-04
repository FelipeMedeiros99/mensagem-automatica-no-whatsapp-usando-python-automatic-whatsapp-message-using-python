from libs.contatos import lista_de_contatos, exibicao_lista_telefonica
from libs.processo_de_envio import gerador_de_links, abrir_conversa, fechar_navegador
from libs.arquivos import busca_texto_e_envia, documento, lista_de_contatos as cont


# criando os documentos antes de tudo para economizar tempo
documento()
cont()

# inserindo os contatos
contatos = lista_de_contatos()

exibicao_lista_telefonica(contatos)

# botão para iniciar
input('pressione Enter para começar')

# juntar o link com o contato
lista_de_links = gerador_de_links(*contatos)

# receber o texto que será enviado

# abrir conversa
contador = 0
for link in lista_de_links:
    if contador == 0:
        abrir_conversa(link, tempo=4)
        contador +=1
        fechar_navegador()
        # buscando o documento com o texto e enviando
        busca_texto_e_envia()

    else:
        abrir_conversa(link)
        # fechando o navegador
        fechar_navegador()
        # buscando o documento com o texto e enviando
        busca_texto_e_envia()
        
