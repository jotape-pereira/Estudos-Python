# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc
n = float(input('punha um numero: '))
print(f'Se botou o {n}, agr tome aqui seu numero inteiro: {trunc(n)}')

