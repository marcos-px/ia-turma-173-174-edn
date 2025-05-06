#contar pares e impares

pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou'fim' para encerrar): ")

    if entrada.lower() == 'fim':
        print("Encerrado com sucesso!")
        break

    try:
        numero = int(entrada)

        if numero % 2 == 0:
            print(f"O número {numero} é par. ")
            pares += 1
        else:
            print(f"O número {numero} é impar.")
            impares += 1

    except ValueError:
        print("Erro: Digite apenas números inteiros")

print("\nResultado: ")
print(f"Números Pares: {pares}")
print(f"Números Impares: {impares}")