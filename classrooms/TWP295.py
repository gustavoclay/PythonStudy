'''Defina um função "embaralha" que retorne as letras de uma string misturadas. Dica:> utilize o list() para converter sua string em lista.'''

def embaralha(lista):
    import random
    lista_emb = list(lista)
    random.shuffle(lista_emb)
    return ''.join(lista_emb)
