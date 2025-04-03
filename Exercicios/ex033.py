# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input('Insira um número: '))
n2 = float(input('Insira mais um número: '))
n3 = float(input('Insira outro número: '))
#if n1 > n2 and n1 > n3:
#    print(f'{n1} é o maior entre {n2} e {n3}')
#elif n2 > n1 and n2 > n3:
#    print(f'{n2} é o maior entre {n1} e {n3}')
#elif n3 > n1 and n3 > n2:
#    print(f'{n3} é o maior entre {n1} e {n2}')

#if n1 < n2 and n1 < n3:
#    print(f'{n1} é o menor entre {n2} e {n3}')
#elif n2 < n1 and n2 < n3:
#    print(f'{n2} é o menor entre {n1} e {n3}')
#elif n3 < n1 and n3 < n2:
#    print(f'{n3} é o menor entre {n1} e {n2}')
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'o maior valor digitado foi {maior}')
print(f'o menor valor digitado foi {menor}')
