import os;

def exibir_nome_do_programa():
    print('Sabor Express \n');

def exibir_opcoes():
    print('1. Cadastrar Restaurante');
    print('2. Listar Restaurantes');
    print('3. Ativar Restaurante');
    print('4. Sair \n');

def finalizar_app():
    os.system('cls')
    print('Encerrando o APP')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '));
    # print(opcao_escolhida == 1);
    # print(type(opcao_escolhida));
    # print(type(1))

    if opcao_escolhida == 1:
        print('Cadastrar Restaurante')
    elif opcao_escolhida == 2:
        print('Listar Restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar Restaurante')
    else:
        finalizar_app();

# opcao_escolhida = int(input('Escolha uma opção: '))
# match opcao_escolhida:
#     case 1:
#         print('Adicionar restaurante')
#     case 2:
#         print('Listar restaurantes')
#     case 3:
#         print('Ativar restaurante')
#     case 4:
#         print('Finalizar app')
#     case _:
#         print('Opção inválida!')

def main():
    exibir_nome_do_programa();
    exibir_opcoes();
    escolher_opcao();
    
if __name__ == '__main__':
    main()