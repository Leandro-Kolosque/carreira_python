# Hora da prática: métodos especiais e atributos
# Em uma carreira de desenvolvimento de software, a prática consistente desempenha um papel fundamental na construção de bases sólidas. Pensando nisso, criamos uma lista de atividades (não obrigatórias) focada em prática para melhorar ainda mais sua experiência de aprendizagem.

# Exercícios
# Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

fusca = Carro(modelo = 'Fusca', cor = 'Azul', ano = 2000)

# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
# Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
class  Restaurante:
    def __init__(self, nome, categoria, capacidade, nota_avaliacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao

    def __str__(self):
        return f'Restaurante {self.nome} | Categoria: {self.categoria}'

restaurante_gaucho = Restaurante(nome = 'Bah', categoria = 'Comida Gaúcha', capacidade = 100, nota_avaliacao = 5)

# Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
# class Restaurantes:
#     def __init__(self, nome, categoria, ativo=False, capacidade, nota_avaliacao):
#         self.nome = nome
#         self.categoria = categoria
#         self.ativo = ativo
#         self.capacidade = capacidade
#         self.nota_avaliacao = nota_avaliacao

# novo_restaurante = Restaurantes(nome='Santa Marmita', categoria='Fast Food')


# Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
class Cliente:
    def __init__(self, nome, idade, email, cpf):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cpf = cpf

cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com', cpf='999.999.999-92')
cliente2 = Cliente(nome='Bob', idade=30, email='bob@gmail.com', cpf='999.999.999-92')
cliente3 = Cliente(nome='Charlie', idade=22, email='charlie@gmail.com', cpf='999.999.999-92')