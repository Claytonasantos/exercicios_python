executa = input('Executa? (sim ou não)')
cont = 0
while executa == 'sim': #variavel de controle do while
    cont+=1
    executa = input('Executar novamente? (sim ou não)')
print(f'O bloco while executou {cont} vezes!')