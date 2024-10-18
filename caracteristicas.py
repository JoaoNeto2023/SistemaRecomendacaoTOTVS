import pandas as pd

# Criar dados de características dos produtos
caracteristicas_produtos = {
    'id_produto': [101, 102, 103, 104],
    'nome_produto': ['Produto A', 'Produto B', 'Produto C', 'Produto D'],
    'categoria': ['Categoria 1', 'Categoria 2', 'Categoria 1', 'Categoria 2'],
    'preco': [10.0, 15.0, 20.0, 25.0]
}

# Criar o DataFrame
df_caracteristicas = pd.DataFrame(caracteristicas_produtos)

# Salvar como CSV
df_caracteristicas.to_csv('dados/caracteristicas_produtos.csv', index=False)
