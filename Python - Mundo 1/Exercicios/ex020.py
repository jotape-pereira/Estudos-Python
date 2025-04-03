# O mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro e mostre a ordem sorteada.

from random import shuffle

a1 = 'Grob'
a2 = 'Glob'
a3 = 'Grod'
a4 = 'Gob'
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'Apresentem o trabalho nessa ordem: {lista}')
