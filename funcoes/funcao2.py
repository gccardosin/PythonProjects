# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica_num (*args):
    total = 1
    for numero in args:
        #total *= numero
        total = total * numero
    return total

multiplica = multiplica_num(1,2,3)

print(multiplica)
        

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar (x):
    if x % 2 ==0:
        return f'O numero {x} é par'
    return f'O numero {x} é impar'


par_ou_impar = par_impar(1)
par_ou_impar = par_impar(2)

