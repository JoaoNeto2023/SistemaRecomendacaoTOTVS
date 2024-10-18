import pandas as pd

# Criar dados históricos com valores numéricos para interações
dados_historicos_numericos = {
    'id_cliente': [1, 1, 2, 2, 3, 3, 1, 2, 3],
    'id_produto': [101, 102, 101, 103, 102, 104, 103, 104, 101],
    'tipo_interacao': [1, 0, 1, 0, 1, 0, 0, 1, 0]  # 1 para compra, 0 para visualização
}

# Criar um DataFrame
df_historicos_numericos = pd.DataFrame(dados_historicos_numericos)

# Salvar como CSV
df_historicos_numericos.to_csv('dados_historicos_numericos.csv', index=False)
