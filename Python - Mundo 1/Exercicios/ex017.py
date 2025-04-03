# Faça um programa que leia o comprimento do cateto oposto e do adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

c_op = float(input('Qual o comprimento do cateto oposto mané? '))
c_ad = float(input('E do adjacente? '))
print(f'Ta aqui sua hipotenusa filha da puta {hypot(c_op, c_ad):.2f}')
