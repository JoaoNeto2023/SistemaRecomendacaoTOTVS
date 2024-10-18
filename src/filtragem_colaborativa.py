import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def filtragem_colaborativa(dados):
    # Criar uma matriz de interação
    matriz_interacao = dados.pivot_table(index='id_cliente', columns='id_produto', values='tipo_interacao', fill_value=0)
    
    # Calcular a similaridade
    matriz_similaridade = cosine_similarity(matriz_interacao)

    print("Matriz de Interação:")
    print(matriz_interacao)
    print("Matriz de Similaridade:")
    print(matriz_similaridade)
    
    return matriz_interacao, matriz_similaridade
