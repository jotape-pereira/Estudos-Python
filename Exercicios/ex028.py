# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
n = int(randint(0, 5))
seu_n = int(input('Qual número eu estou pensando? '))
if seu_n == n:
    print(f'Exato, eu pensei em {n}')
else:
    print(f'Errado, na realidade eu pensei em {n} e não no {seu_n}')
