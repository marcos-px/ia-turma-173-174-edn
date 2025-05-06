#utilizo o break para interromper o laço quando o índice for igual a 5

for i in range(1,11):
    if i == 8: # Quando o índice for igual a 5, o loop é completamente interrompido
        break
    print(i)