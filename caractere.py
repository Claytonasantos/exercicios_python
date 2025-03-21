var = input("Digite o caractere: ")

if var.isdigit():
    resultado = f"{var} é um número"
else:    
    if var.isupper():
        resultado = f"{var} é maiúsculo"
    else:
        resultado = f"{var} é minúsculo"

print(f"A palavra é: {resultado}")
