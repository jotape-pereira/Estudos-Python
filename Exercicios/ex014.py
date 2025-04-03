# Crie um programa que irá converter a temperatura de graus célsius para outras medidas

celsius = float(input('Qual a temperatura em °C: '))
print(f'{celsius} °C convertido em:\nFahrenheit: {(celsius*9/5)+32} °F\nKelvin: {celsius+273.15} K')