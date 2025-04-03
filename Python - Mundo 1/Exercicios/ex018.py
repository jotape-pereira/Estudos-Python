# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, tan, cos, radians

n = float(input('Punha o grau ai meu chapa: '))
convert = radians(n)
print(f'O valor dessa merda são os seguintes:\nSeno = {sin(convert):.3f}\nCosseno = {cos(convert):.3f}\nTangente = {tan(convert):.3f}')
