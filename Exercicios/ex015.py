# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado

val_aluguel = 60
val_km = 0.15
dias = int(input('Quantos dias de aluguel? '))
kms_rodados = float(input('Quantos KMs rodados?'))
print(f'O total a pagar pelo aluguel é: R${(dias*val_aluguel)+(kms_rodados*val_km)}')
