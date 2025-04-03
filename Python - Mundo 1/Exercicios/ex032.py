# Faça um programa que leia um ano qualquer e diga se ele é um ano bissexto
from datetime import date 
ano = int(input('Digite um ano (Para analisar o ano atual coloque 0): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f' o ano {ano} é bissexto')
else:
    print(f'o ano {ano} não é bissexto')
    