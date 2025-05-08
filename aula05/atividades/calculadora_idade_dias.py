import datetime

def calcular_idade_em_dias(ano_nascimento):
    """
    CALCULA A IDADE DA PESSOAS EM DIAS (APROXIMADO)
    
    Params:
        ano_nascimento (int)
    
    Return:
        int: A idade aproxiamda em dias
    """

    #Obtendo o ano atual

    ano_atual = datetime.datetime.now().year

    idade_anos = ano_atual - ano_nascimento

    idade_dias = idade_anos * 365

    return idade_dias

try:
    ano = int(input("Digite o ano de nascimento: "))

    if ano > datetime.datetime.now().year:
        print("Erro: Ainda não inventamos a máquina do tempo! Não pode colocar um ano no futuro")
    else:
        dias = calcular_idade_em_dias(ano)
        print(f"Sua idade aproximada em dias é: {dias} dias.")

except ValueError:
    print("Erro: Digite um ano válido")