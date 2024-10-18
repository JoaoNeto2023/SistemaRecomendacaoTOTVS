import pandas as pd

def carregar_dados(caminho_arquivo):
    # Carregar os dados
    dados = pd.read_csv(caminho_arquivo)
    return dados

def preprocessar_dados(dados):
    # Remover dados duplicados
    dados.drop_duplicates(inplace=True)
    
    # Tratar valores ausentes
    dados.fillna(0, inplace=True)
    
    # Mapeamento da coluna tipo_interacao para valores numéricos
    dados['tipo_interacao'] = dados['tipo_interacao'].map({'compra': 1, 'visualizacao': 0})
    
    return dados

if __name__ == "__main__":
    dados = carregar_dados('dados/dados_historicos.csv')
    dados_processados = preprocessar_dados(dados)
    dados_processados.to_csv('dados/dados_processados.csv', index=False)
