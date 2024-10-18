import pandas as pd

# Criar dados de interações
dados_interacoes = {
    'id_cliente': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5],
    'id_produto': [101, 102, 103, 101, 102, 104, 103, 105, 106, 102, 104, 101, 105, 106],
    'tipo_interacao': ['compra', 'visualizacao', 'compra', 
                       'visualizacao', 'compra', 'visualizacao', 
                       'compra', 'visualizacao', 'compra', 
                       'visualizacao', 'compra', 'compra', 
                       'visualizacao', 'compra']
}

# Criar um DataFrame para interações
df_interacoes = pd.DataFrame(dados_interacoes)

# Salvar como CSV
df_interacoes.to_csv('dados/dados_historicos.csv', index=False)

# Criar dados de características dos produtos
dados_produtos = {
    'id_produto': [101, 102, 103, 104, 105, 106],
    'nome_produto': ['Protheus', 'DataSul', 'TechFin', 'Business', 'Customização', 'T-Cloud'],
    'categoria': ['Categoria 1', 'Categoria 2', 'Categoria 1', 'Categoria 2', 'Categoria 1', 'Categoria 2'],
    'preco': [10.0, 15.0, 20.0, 25.0, 30.0, 35.0]
}

# Criar um DataFrame para características dos produtos
df_produtos = pd.DataFrame(dados_produtos)

# Salvar como CSV
df_produtos.to_csv('dados/caracteristicas_produtos.csv', index=False)

