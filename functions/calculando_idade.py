# REVISÃO DEDICADA A FUNÇÕES

#Calculando a idade
# Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento. Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.

def calcular_idade(ano_nasc, ano_atual):
    return ano_atual - ano_nasc

nascimento = int(input("Digite o ano de nascimento: ")) 
atual = int(input("Digite o ano atual: ")) 
idade = calcular_idade(nascimento, atual) 
print(f"A idade é {idade} anos.") 