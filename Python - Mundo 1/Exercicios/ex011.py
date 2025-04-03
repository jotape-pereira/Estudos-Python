# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

larg = float(input('Qual largura da parede? '))
alt = float(input('Qual altura? '))
area = larg*alt
print(f'Numa area de {area}m² seria necessário {area/2}L de tintas para pintar por inteiro.')