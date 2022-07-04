# contatos
def modelo_de_contato(numero):
    # recebe apenas os números que forem digitados, ignrando os caracteres especiais
    numero = str(numero)
    contato = [digito for digito in numero if digito.isdigit()]
    if len(contato) == 10:
        contato.insert(2, '9')
    if len(contato) == 11:
        return ''.join(contato)
    else:
        return False


def exibe_contato(contato):
    contato = str(contato)
    # retorna o contato de forma bonita
    return f'({contato[0:2]}){contato[2:7]}-{contato[7:12]}'


def exibe_lista_telefonica(lista):
    # exibindo a lista telefônica e mostrando a posição de cada contato
    [print(f'{pos +1} - {exibe_contato(contato)}') for pos, contato in enumerate(lista)]


def lista_de_contatos():
    from arquivos import lista_de_contatos as contatos
    lista_telefonica = []
    for numeros in contatos():
        numero = modelo_de_contato(numeros)
        if not numero:
            print(f'o número {numeros} é inválido, verifique-o')
        else:
            lista_telefonica.append(numero)

    return lista_telefonica


def exibicao_lista_telefonica(txt):
    print('-='*24)
    exibe_lista_telefonica(txt)
    print('-=' * 24)
