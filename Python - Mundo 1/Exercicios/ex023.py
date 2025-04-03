# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# EX: 
#    Digite um número: 1834

#    Unidade: 4
#    Dezena: 3
#    Centena: 8
#    Milhar: 1
n = int(input('Punha um numero: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Seu numero: {n}\nUnidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar: {m}')