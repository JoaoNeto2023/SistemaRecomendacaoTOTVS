#Código para pré-processamento dos dados

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
    return dados

if __name__ == "__main__":
    dados = carregar_dados('dados/dados_historicos.csv')
    dados_processados = preprocessar_dados(dados)
    dados_processados.to_csv('dados/dados_processados.csv', index=False)
