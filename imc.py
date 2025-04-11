peso = int(input('digite o peso: '))
altura = float(input('digite a altura:'))

imc = peso/altura**2

if imc < 26:
    print('grau: normal')
elif imc>=26 and imc<30:
    print('grau: obeso')
elif imc >=30:
    print('grau: obeso morbido')

print(f"{imc}")
