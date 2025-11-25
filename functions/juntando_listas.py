# REVISÃO DEDICADA A FUNÇÕES

#Juntando listas de produtos

# Clara está gerenciando o estoque de sua loja e recebeu duas listas separadas: uma contendo os nomes dos produtos e outras com seus respectivos preços. Para facilitar a organização, ela precisa combinar essas listas de forma que cada produto seja associado ao seu preço.
# Crie um programa que junte as listas e exiba o resultado no formato produto: preço

nome_produto = input('Digite o nome do produto separado por vírgula').split(",") ;
preco_produto = input('Digite o preço do produto separado por vírgula').split(",") ;

for produto, preco in zip(nome_produto, preco_produto): 
    print(f"{produto.strip()}: {preco.strip()}") 
