# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

value = float(input('quanto custa essa brincadeira ai? '))
perc_desc = float(input('percentual de desconto: '))
calc_desc = value*perc_desc/100
print(f'Valor original R${value}\nDesconto: {perc_desc:.0f}%\nTotal com desconto: R${value-calc_desc:.2f}')
