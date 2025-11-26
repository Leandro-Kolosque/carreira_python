# Jogo de adivinhar o número

# Maria está criando um jogo para seus alunos praticarem lógica e pensamento rápido. Ela quer um programa onde o computador escolhe um número aleatório entre 1 e 100, e o jogador tem que adivinhar qual é.
# Além de garantir a jogabilidade, Maria deseja que o programa trate erros de entrada, impedindo que o usuário forneça valores inválidos, como letras ou números fora do intervalo permitido.
# Sua tarefa é criar um programa que gere um número aleatório entre 1 e 100 e permita que o usuário tente adivinhar o número. O programa deve informar se o palpite é maior ou menor que o número correto, até que o usuário acerte. Se o usuário digitar um valor inválido ou um número fora do intervalo, uma exceção ValueError deve ser lançada.
import random

def escolha_numero():
    escolha_computador = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
            escolha_jogador = int(input('Escolha um número entre 1 e 100: '))

            if not 1 <= escolha_jogador <= 100:
                raise ValueError('Número fora do intervalo! Digite um número entre 1 e 100.')
        
            tentativas += 1

            if escolha_jogador < escolha_computador:
                print('Muito baixo! Tente novamente.')
            elif escolha_jogador > escolha_computador:
                print('Muito alto! Tente novamente.')
            else:
                print(f'Parabéns você acertou com {tentativas} tentativas')
                break

        except ValueError as e:
            print(f'Entrada inválida: {e}')

escolha_numero()


