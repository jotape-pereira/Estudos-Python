# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
r1 = float(input('Insira um número: ')) 
r2 = float(input('Insira outro: '))
r3 = float(input('Insira mais um: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Com essas medidas você consegue formar um triângulo.')
else:
    print('Com essas medidas não dá para formar um triângulo')