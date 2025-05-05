#Trata erro de conversão de tipo

try:
    # Código que pode gerar um erro
    numero = int(input("Digite um número: "))
    print(f"Você digitou o número {numero}")
except ValueError:
    # Código executado se der erro
    print("Isso não é um número inteiro! Por favor, verifique!")