# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

# Meu code abaixo ficou fei, então otimizei com o do irmão
#city = str(input('punha uma city: '))
#separar = city.upper().split()
#verify = 'SANTO' in separar[0]
#print(f'Primeiro nome é santo? {verify}')

city = str(input()).strip()
print(city[:5].upper() == 'SANTO')
