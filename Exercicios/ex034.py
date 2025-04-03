# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumneto.
# Para salários superiores a R$1250,00 , calcule um aumento de 10%
# Para os inferiores ou iguais o aumento é de 15%
sal = float(input('Insira o seu salário: '))
if sal > 1250:
    perc_desc = 10
    calc_desc = sal*perc_desc/100
    print(f'Seu salário teve um aumento de {perc_desc}%')
    print(f'A receber antes: R$ {sal:.2f}')
    print(f'A receber agora: R$ {sal+calc_desc:.2f}')
else:
    perc_desc = 15
    calc_desc = sal*perc_desc/100
    print(f'Seu salário teve um aumento de {perc_desc}%')
    print(f'A receber antes: R$ {sal:.2f}')
    print(f'A receber agora: R$ {sal+calc_desc:.2f}')
