def calculo_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Esta função calcula o valor da gorjeta baseado no total da conta e da porcentagem.

    Parâmetros:
        valor_conta (float): O valor total da conta
        porcentagem_gorjeta (float): Porcentagem da gorjeta

    Retorna:
        float: O valor da gorjeta calculada
    """

    gorjeta = valor_conta * (porcentagem_gorjeta / 100)

    return round(gorjeta, 2)

total_conta = float(input("Informa o total da conta: "))
porcentagem = float(input("Informe a porcentagem da gorjeta: "))

valor_gorjeta = calculo_gorjeta(total_conta, porcentagem)

print(f"Para uma conta de {total_conta:.2f}, a gorjeta de {porcentagem}% tem o valor de R${valor_gorjeta}")