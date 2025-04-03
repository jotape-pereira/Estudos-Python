# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

a1 = 'Grob'
a2 = 'Glob'
a3 = 'Grod'
a4 = 'Gob'
lista = [a1, a2, a3, a4]
print(f'{choice(lista)}! vai apagar a lousa !')