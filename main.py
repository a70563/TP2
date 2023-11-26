from clientes import cria_novo_cliente, imprime_lista_de_clientes
from faturas import cria_nova_fatura, imprime_lista_de_faturas
from io_ficheiros import (carrega_as_listas_dos_ficheiros,
                          guarda_as_listas_em_ficheiros)
from io_terminal import pause
from veiculos import cria_novo_veiculo, imprime_lista_de_veiculos
from item import cria_novo_item, imprime_lista_de_items
from cortesia import cria_novo_viatura_cortesia, imprime_lista_de_cortesia


def menu():
    """Menu principal da aplicação de oficina"""

    lista_de_veiculos = []
    lista_de_clientes = []
    lista_de_items = []
    lista_de_faturas = []
    lista_de_cortesia = []

    while True:
        print("""
        *********************************************************************
        :  (-: OFICINA WINRAR - ZIPAMOS QUALQUER ARRANJO NUM INSTANTE :-)   :
        *********************************************************************
        :                                                                   :
        : nc  - Novo Cliente            lc  - Listagem de Clientes          :
        : nv  - Novo Veiculo            lv  - Listagem de Veiculos          :
        : nf  - Mova Fatura             lf  - Listagem das Faturas          :
        : ni  - Novo Item               li  - Listagem de Items             :
        : nvc - Nova Viatura Cortesia   lvc - Listagem Viaturas de Cortesia :
        : ...                                                               :
        : g - guarda tudo           c - carrega tudo                        :
        : x - sair                                                          :
        :                                                                   :
        *********************************************************************
        """)

        op = input("opcao?").lower()

        if op == "x":
            exit()

        elif op == "g":
            guarda_as_listas_em_ficheiros(lista_de_veiculos, lista_de_clientes, lista_de_faturas, lista_de_items, lista_de_cortesia)

        elif op == "c":
            lista_de_veiculos, lista_de_clientes, lista_de_faturas, lista_de_items, lista_de_cortesia = carrega_as_listas_dos_ficheiros()

        elif op == "nc":
            novo_cliente = cria_novo_cliente()
            if novo_cliente is not None:
                lista_de_clientes.append(novo_cliente)

        elif op == "nv":
            novo_veiculo = cria_novo_veiculo()
            if novo_veiculo is not None:
                lista_de_veiculos.append(novo_veiculo)

        elif op == "ni":
            novo_item = cria_novo_item()
            if novo_item is not None:
                lista_de_items.append(novo_item)

        elif op == "nvc":
            novo_viatura_cortesia = cria_novo_viatura_cortesia()
            if novo_viatura_cortesia is not None:
                lista_de_cortesia.append(novo_viatura_cortesia)

        elif op == "nf":
            if len(lista_de_clientes) == 0 or len(lista_de_veiculos) == 0:
                print("Não há clientes ou veiculos registados...")
                continue

            nova_fatura = cria_nova_fatura(lista_de_clientes, lista_de_veiculos, lista_de_items)
            lista_de_faturas.append(nova_fatura)

        elif op == "lc":
            imprime_lista_de_clientes(lista_de_clientes)
            pause()

        elif op == "lv":
            imprime_lista_de_veiculos(lista_de_veiculos)
            pause()

        elif op == "lf":
            imprime_lista_de_faturas(lista_de_faturas)
            pause()
    
        elif op == "li":
            imprime_lista_de_items(lista_de_items)
            pause()

        elif op == "lvc":
            imprime_lista_de_cortesia(lista_de_cortesia)
            pause()


if __name__ == "__main__":
    menu()