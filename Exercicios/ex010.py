# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

from babel.numbers import format_currency

r = float(input('Quanto se tem na carteira? '))
d = float(r/5.752)
real = format_currency(r, 'BRL')
dolar = format_currency(d, 'USD')

print(f'com essa mixaria {real} você compra {dolar}')
