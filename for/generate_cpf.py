import random

entrada = input('deseja gerar quantos cpfs? ')
entrada_int = 0

try:
    entrada_int = int(entrada)
except NameError:
    print('Isso não é um número inteiro')
except ValueError:
    print('Isso não é um número inteiro')
    
for i in range(entrada_int):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    contador_regressivo_1 = 10
    resultado_1 = 0

    for digito in nove_digitos:
        resultado_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
        
    digito_1 = resultado_1 * 10 % 11 
    digito_1 =  digito_1 if digito_1 <= 9 else 0

    #print (digito_1)

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11
    resultado_2 = 0

    for digito in dez_digitos:
        resultado_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
        
    digito_2 = resultado_2 * 10 % 11
    digito_2 = digito_2 if digito_2 <=9 else 0

    #print (digito_2)

    cpf_check = f'{nove_digitos}{digito_1}{digito_2}'

    print(f'seu cpf gerado é: {cpf_check}')
