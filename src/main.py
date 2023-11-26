from clientes import cria_novo_cliente, imprime_lista_de_clientes
from faturas import cria_nova_fatura, imprime_lista_de_faturas
from io_ficheiros import (carrega_as_listas_dos_ficheiros, guarda_as_listas_em_ficheiros)
from io_terminal import pause
from veiculos import cria_novo_veiculo, imprime_lista_de_veiculos
from item import cria_novo_item, imprime_lista_de_items
from cortesia import cria_novo_veiculo_cortesia, imprime_lista_de_cortesia


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
        : NC  - Novo Cliente            LC  - Listagem de Clientes          :
        : NV  - Novo Veiculo            LV  - Listagem de Veiculos          :
        : NF  - Nova Fatura             LF  - Listagem das Faturas          :
        : NI  - Novo Item               LI  - Listagem de Items             :
        : NVC - Nova Veículos Cortesia  LVC - Listagem Veículos de Cortesia :
        : ...                                                               :
        : G - guarda tudo           C - carrega tudo                        :
        : X - sair                                                          :
        :                                                                   :
        *********************************************************************
        """)

        op = input("Opcao? ").upper()

        if op == "X":
            exit()

        elif op == "G":
            guarda_as_listas_em_ficheiros(lista_de_veiculos, lista_de_clientes, lista_de_faturas, lista_de_items, lista_de_cortesia)

        elif op == "C":
            lista_de_veiculos, lista_de_clientes, lista_de_faturas, lista_de_items, lista_de_cortesia = carrega_as_listas_dos_ficheiros()

        elif op == "NC":
            novo_cliente = cria_novo_cliente()
            if novo_cliente is not None:
                lista_de_clientes.append(novo_cliente)

        elif op == "NV":
            novo_veiculo = cria_novo_veiculo()
            if novo_veiculo is not None:
                lista_de_veiculos.append(novo_veiculo)

        elif op == "NV":
            novo_item = cria_novo_item()
            if novo_item is not None:
                lista_de_items.append(novo_item)

        elif op == "NVC":
            novo_veiculo_cortesia = cria_novo_veiculo_cortesia()
            if novo_veiculo_cortesia is not None:
                lista_de_cortesia.append(novo_veiculo_cortesia)

        elif op == "NF":
            if len(lista_de_clientes) == 0 or len(lista_de_veiculos) == 0:
                print("Não há clientes ou veiculos registados...")
                continue

            nova_fatura = cria_nova_fatura(lista_de_clientes, lista_de_veiculos, lista_de_items)
            lista_de_faturas.append(nova_fatura)

        elif op == "LC":
            imprime_lista_de_clientes(lista_de_clientes)
            pause()

        elif op == "LV":
            imprime_lista_de_veiculos(lista_de_veiculos)
            pause()

        elif op == "LF":
            imprime_lista_de_faturas(lista_de_faturas)
            pause()
    
        elif op == "LI":
            imprime_lista_de_items(lista_de_items)
            pause()

        elif op == "LVC":
            imprime_lista_de_cortesia(lista_de_cortesia)
            pause()


if __name__ == "__main__":
    menu()