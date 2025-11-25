# Contagem de vogais em um texto

# Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto digitado pelos alunos. Isso ajudará a analisar a estrutura das palavras utilizadas.
# Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.
import unicodedata

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def contador_vogais(texto):
    texto_sem_acentos = remover_acentos(texto.lower())
    vogais = "aeiou"
    return sum(1 for letra in texto_sem_acentos if letra in vogais)

texto = input('Digite um texto: ')
print(f"O texto contém {contador_vogais(texto)} vogais.")

