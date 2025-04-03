# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
n = str(input('punha nome: '))
verify = 'SILVA' in n.upper()
print(f'tem silva? {verify}')