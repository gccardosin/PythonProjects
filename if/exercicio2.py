nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'seu nome é: {nome}')
   
    print(f'seu nome invertido é: {nome[::-1]}')
    
    if ' ' in nome:
        print(f'seu nome tem {nome.count(" ")} espaços')
    else:
        print(f'seu nome não tem espaços')    
    
    print(f'A primeira letra do seu nome é: {nome[0]}')
    
    print(f'seu nome tem {len(nome)} letras')
    
    print(f'A ultima letra do seu nome é: {nome[-1]}')
else:
    print('você deve digitar um nome e uma idade')