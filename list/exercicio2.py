import os

"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista_compra = []

while True:
    opcao = input('Selecione sua opção: [1] Inserir [2] Apagar [3] Listar [4] Sair: ')
    
    if opcao == '1':
        os.system('cls')
        inserir = input('Escreva um item: ')
        lista_compra.append(inserir)
        continue
   
    elif opcao == '2':
        apagar_indice = input('Escreva um indice para apagar: ')
        try:
            apagar_indice_inteiro = int(apagar_indice)
            del lista_compra[apagar_indice_inteiro]           
        except:
            print('Entre com um indice correto')
            continue
    
    elif opcao == '3':
        os.system('cls')
        for i in enumerate(lista_compra):
            print (i)
        continue
    
    elif opcao == '4':
        print ('Você escolheu sair')
        break
    
    else:
        print('Opção inválida')
        continue
    
    
"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')