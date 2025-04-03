# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite
vel = float(input('Velocidade: '))
if vel > 80:
    multa = (vel - 80) * 7
    print(f'Velocidade: {vel:.0f}Km/h\nExcedeu o limite de velocidade, você foi multado!\nValor da multa: R$ {multa:.2f}')
else:
    print('Está dirigindo de forma segura, continue assim!')
