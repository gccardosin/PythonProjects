# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiplicador(multiplicador):
    def multiplica(numero):
        return numero*multiplicador
    return multiplica

triplicar = multiplicador(3)

print(triplicar(3))
