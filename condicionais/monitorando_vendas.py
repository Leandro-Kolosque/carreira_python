# REVISÃO DEDICADA A CONDICIONAIS

# Monitorando vendas no comércio
# Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.

# Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.
numero_vendas_bananas = int(input('Digite o número de vendas de Bananas: '));
numero_vendas_maca = int(input('Digite o número de vendas de Maças: '));

if numero_vendas_bananas > numero_vendas_maca:
    print('O número de vendas de Bananas foi maior que o número de vendas de Maças');
elif numero_vendas_bananas < numero_vendas_maca:
    print('O número de vendas de Maças foi maior que o número de vendas de Bananas');
elif numero_vendas_bananas == numero_vendas_maca:
    print('Ambos os produtos tiveram o mesmo número de vendas');
else:
    print('Não foi possivel calcular as vendas dos produtos')