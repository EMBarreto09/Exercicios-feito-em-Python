#Erros e exceções

from uteis_erros import leia_int, leia_float


i = leia_int('Digite um número inteiro: ')
d = leia_float('Digite um número decimal: ')
print(f'\033[1;32mO número inteiro é {i}, e o número decimal é {d}\033[m')