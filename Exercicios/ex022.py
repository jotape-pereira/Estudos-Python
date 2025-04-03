# Crie um programa que leia o nome completo de uma pessoa e mostre:
#  > O nome com todas letras maiúsculas / minúsculas
#  > Quantas letras ao todo (sem considerar espaços)
#  > Quantas letras tem o primeiro nome

nome = str(input('Punha um nome ai seu fanfarrão: '))
space = nome.count(' ')
print(f'Maiúsculas: {nome.upper()}\nMinúsculas: {nome.lower()}\nTotal de letras nesse nome: {len(nome)-space}\nTotal letras primeiro nome: {len(nome.split()[0])}')
