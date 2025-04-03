# Crie um programa que leia um número inteiro que mostre na tela se ele é PAR ou IMPAR.
n = int(input('Digite um número: '))
p = n / 2
print(n)
if p.is_integer() == True:
    print(f'O Número {n} é par.')
else:
    print(f'O número {n} é ímpar.')