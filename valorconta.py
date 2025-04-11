kw = float(input("digite o total de KW consumidos: "))
valorminimo = 11.90

if kw < 150:
    valorconta = valorminimo + (kw * 0.20)
    print (f'o valor da conta é : {valorconta}')
elif kw >=150 and kw<300:
    valorconta = valorminimo + (kw * 0.25)
    print (f'o valor da conta é: {valorconta}')
else:
    valorconta = valorminimo + (kw * 0.30)
    print (f'o valor da conta é: {valorconta}')
