frase = 'aaaaab'

i = 0
contador = 0
letra_mais_frequente = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    contagem_letras = frase.count(letra_atual)

    if contador < contagem_letras:
        contador = contagem_letras
        letra_mais_frequente = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_mais_frequente}" que apareceu '
    f'{contador}x'
)