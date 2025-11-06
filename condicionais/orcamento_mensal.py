# REVISÃO DEDICADA A CONDICIONAIS

# Controlando o orçamento mensal
# Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. 
# O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.

total_despesas = float(input('Digite o seu gasto mensal em reais. R$:'))

if total_despesas > 3000:
    print(f'Você teve um total de despesas igual a: R${total_despesas}, portanto você passou do limite estipulado de R$3000')
else:
    print(f'Você teve um total de despesas igual a: R${total_despesas}, portanto você ainda está dentro do limite estipulado')