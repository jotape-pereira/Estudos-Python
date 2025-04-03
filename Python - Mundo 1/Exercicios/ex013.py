# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('quanto que o colega ganha por mês? '))
perc_desc = float(input('percentual de desconto: '))
calc_desc = salario*perc_desc/100
print(f'O amigo tava ganhando R${salario} p/mês, recebeu um aumento de {perc_desc:.0f}% e agora ganha R${salario+calc_desc:.2f} p/ mês, estouro !')


