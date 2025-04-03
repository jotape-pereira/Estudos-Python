# Faça um programa que leia uma frase pelo teclado e mostre:
# > Quantas vezes aparece a letra "A"
# > Em que posição ela aparece a primeira vez.
# > Em que posição ela aparece a última vez.
txt = str(input('escreva uma frase: ')).strip()
print(f'Quantas letras "A" tem ai? {txt.upper().count("A")}\nQuando ela aparece a primeira vez? {txt.upper().find("A")+1}\nE por último? {txt.upper().rfind("A")+1}')
