from sys import path

import modulos.pkg_modulo
from modulos import pkg_modulo
from modulos.pkg_modulo import *

# from aula99_package.modulo import soma_do_modulo

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(modulos.pkg_modulo.soma_do_modulo(1, 2))
print(pkg_modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)