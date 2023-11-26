from tabulate import tabulate

def imprime_lista(cabecalho, lista):
    """Imprime a :attr:`lista` na forma de uma tabela com um cabeçalho

    Recebe uma lista na forma [{"atrib1": valor1, "atrib2": valor2, ...},
    {"atrib1": valor1, "atrib2": valor2, ...}, ...] e imprime no terminal uma tabela
    na forma

    ==  ======  ======
    id  atrib1  atrib2
    ==  ======  ======
    0   valor1  valor2
    1   ...      ...
    ==  ======  ======

    :param cabecalho: Cabecalho para a listagem
    :param lista: Lista a ser impressa
    """

    print(cabecalho)

    if (len(lista) == 0):
        print("Lista vazia")
    else:
        # cabecalho da tabela
        lista_a_imprimir = [["id"] + list(lista[0].keys())]
        # dados
        lista_a_imprimir.extend([[id] + list(d.values()) for id, d in enumerate(lista)])

        print(tabulate(lista_a_imprimir, headers="firstrow", tablefmt='psql'))


def pause():
    """Faz uma pausa no programa e espera que o utilizador pressione ENTER"""

    input("Pressione ENTER para continuar...")


def pergunta_id(questao, lista, mostra_lista=False):
    """TODO: documentação

    :param questao: qual o ID do cliente e do veiculo para ser colocado na fatura
    :param lista: lista de cliente e lista de veiculo
    :param mostra_lista: mostra a lista de clientes e a lista de veiculos
    :return:
    """

    if mostra_lista:
        imprime_lista(cabecalho="", lista=lista)

    while True:
        id = int(input(questao))
        if 0 <= id < len(lista):
            return id
        else:
            print(f"id inexistente. Tente de novo. Valores admitidos {0} - {len(lista)}")

def guarda_as_listas_em_ficheiros(lista_de_veiculos, lista_de_clientes, lista_de_faturas, lista_de_items, lista_de_cortesia):
    """TODO: documentação

    :param lista_de_clientes: lista de clientes registados e guardados
    :param lista_de_veiculos: lista de veiculos registados e guardados
    :param lista_de_faturas: lista de faturas feitas e guardadas
    """