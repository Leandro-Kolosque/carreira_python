class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

#Para criar novo restaurante
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]
print(vars(restaurante_praca))

# Exercícios
# Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_pizza da classe Restaurante.
restaurante_pizza.categoria = 'Italiana'

# Acesse o valor do atributo nome da instância restaurante_pizza da classe Restaurante.
nome_do_restaurante = restaurante_pizza.nome

# Verifique o valor inicial do atributo ativo para a instância restaurante_pizza e exiba uma mensagem informando se o restaurante está ativo ou inativo.
if restaurante_pizza.ativo == True:
    print('Restaurante Ativo')
else:
    print('Restaurante Inativo')

# Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
categoria = Restaurante.categoria

# Altere o valor do atributo nome para 'Bistrô'.
restaurante_praca.nome = 'Bistrô'

# Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

# Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')

# Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True

# Imprima no console o nome e a categoria da instância restaurante_praca.
print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')