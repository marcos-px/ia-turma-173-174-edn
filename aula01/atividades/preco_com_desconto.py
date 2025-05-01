preco = 1000 #valor do produto
desconto = 15 #valor do desconto

valor_final = preco - (preco * desconto / 100) #formula do desconto
print(f"\nO preço do celular de Maria com {desconto}% de desconto é R${valor_final}")