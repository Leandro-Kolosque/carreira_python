# Calculadora com tratamento de erros

# Carlos está criando uma calculadora simples, mas quer garantir que o programa não quebre se o usuário digitar valores inválidos, ele precisa tratar os erros.
# Crie uma calculadora que permita ao usuário escolher entre soma, subtração, multiplicação e divisão. Além de modularizar o código em funções, use try-except para tratar erros de entrada inválida, que consiste em:
# Caso digite um caractere em vez de número | exceção a ser lançada: ValueError;
# Caso tente fazer uma divisão por 0 | exceção a ser lançada: ZeroDivisionError.

def somar(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

def calculadora():
    try:
        num1 = float(input('Digite o primeiro valor: '))
        operacao = input('Escolha a operação (+, -, *, /): ')
        num2 = float(input('Digite o segundo valor: '))

        if operacao == '+':
            resultado = somar(num1, num2)
        elif operacao == '-':
            resultado = subtracao(num1, num2)
        elif operacao == '*':
            resultado = multiplicar(num1, num2)
        elif operacao == '/':
            resultado = divisao(num1, num2)
        else:
            print('Operação Inválida')
            return

        print(f'Resultado = {resultado}')

    except ValueError:
        print('Erro: Entrada de Dados Inválida. Digite apenas números')

    except ZeroDivisionError:
        print('Erro: Divisão por zero não é permitida')

calculadora()
    