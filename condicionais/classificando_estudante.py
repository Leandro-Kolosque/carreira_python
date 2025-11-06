# REVISÃO DEDICADA A CONDICIONAIS

# Classificando estudantes por média
# Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:

# Média >= 7: Aprovado
# 5 <= Média < 7: Recuperação
# Média < 5: Reprovado
# Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.

nota01 = float(input('Digite a primeira nota: '));
nota02 = float(input('Digite a segunda nota: '));
nota03 = float(input('Digite a terceira nota: '));

media = (nota01 + nota02 + nota03) / 3

if media >= 7:
    print('O aluno está aprovado')
elif media <= 5 and media < 7:
    print('O aluno está de recuperação')
elif media < 5:
    print('O aluno está reprovado')
else:
    print('Erro!')
    