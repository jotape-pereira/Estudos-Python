# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro = Ana
# último = Souza
n = str(input('punha seu nome meu fi: ')).strip()
print(f'Primeiro nome: {n.split()[0]}\nUltimo nome: {n.split()[-1]}')
