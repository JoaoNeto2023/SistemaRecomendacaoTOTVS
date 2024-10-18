import pandas as pd
from filtragem_colaborativa import filtragem_colaborativa
from filtragem_baseada_conteudo import filtragem_baseada_conteudo

def recomendar_produtos(id_cliente, dados):
    # Carregar características dos produtos para mapear ID -> Nome
    caracteristicas_produtos = pd.read_csv('dados/caracteristicas_produtos.csv', index_col='id_produto')
    
    # Obter matriz de interação e similaridade
    matriz_interacao, matriz_similaridade = filtragem_colaborativa(dados)

    print("Número de clientes:", len(matriz_similaridade))
    print("ID do cliente:", id_cliente)

    # Verifica se o id_cliente é válido
    if 1 <= id_cliente <= len(matriz_similaridade):  # Verifica se o índice está dentro do limite
        similaridade_cliente = matriz_similaridade[id_cliente - 1]  # Índice baseado em 0
        print("Similaridade do Cliente:", similaridade_cliente)

        # Verificar quais clientes são mais similares ao cliente atual
        clientes_similares = similaridade_cliente > 0
        print(f"Clientes Similares: {clientes_similares}")

        # Selecionar produtos dos clientes similares (excluindo os do cliente atual)
        produtos_recomendados = []
        for idx, is_similar in enumerate(clientes_similares):
            if is_similar and idx != id_cliente - 1:
                # Pegar os produtos que o cliente similar interagiu
                produtos_similares = matriz_interacao.iloc[idx]
                produtos_recomendados.extend(produtos_similares[produtos_similares > 0].index.tolist())

        print(f"Produtos Recomendados com base na filtragem colaborativa: {produtos_recomendados}")

        # Obter recomendações baseadas em conteúdo
        recomendacoes_conteudo = filtragem_baseada_conteudo(dados)

        # Combinar as recomendações de conteúdo com as recomendações colaborativas
        recomendacoes = set(recomendacoes_conteudo)  # Usar um conjunto para evitar duplicatas
        recomendacoes.update(produtos_recomendados)  # Adicionar os produtos recomendados via colaboração

        # Mapear os IDs dos produtos para seus respectivos nomes
        nomes_produtos_recomendados = [caracteristicas_produtos.loc[id_produto, 'nome_produto'] for id_produto in recomendacoes]
        return nomes_produtos_recomendados  # Retornar a lista de nomes de produtos
    else:
        print("ID do cliente fora do limite.")
        return []

if __name__ == "__main__":
    dados = pd.read_csv('dados/dados_processados.csv')
    id_cliente = 1  # Exemplo de ID de cliente
    recomendacoes = recomendar_produtos(id_cliente, dados)
    print("Produtos Recomendados para o Cliente", id_cliente, ":\n", recomendacoes)
