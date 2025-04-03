# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
dist = float(input('Qual a distância de sua viagem? '))
if dist <= 200:
    print(f'Você irá viajar por {dist:.0f}Km.\nO valor de sua passagem é: R$ {dist*0.5:.2f}')
else:
    print(f'Você irá viajar por {dist:.0f}Km.\nO valor de sua passagem é: R$ {dist*0.45:.2f}')
