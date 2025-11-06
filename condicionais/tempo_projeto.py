# REVISÃO DEDICADA A CONDICIONAIS

# Calculando o tempo total de projeto
# Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.

# Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.
dias_atividade_a = int(input('Digite o número de dias que a atividade demorou '));
dias_atividade_b = int(input('Digite o número de dias que a atividade demorou '));
dias_atividade_c = int(input('Digite o número de dias que a atividade demorou '));

total_de_dias_da_atividade = dias_atividade_a + dias_atividade_b + dias_atividade_c;
if total_de_dias_da_atividade > 0:
    print(f'O número total de dias foi igual a {total_de_dias_da_atividade}')
else:
    print('Número de dias inválidos, por favor insira números positivos');