import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sistema_recomendacao import recomendar_produtos  # Importe sua função de recomendação

def exibir_recomendacoes():
    try:
        id_cliente = int(entry_id_cliente.get())
        dados = pd.read_csv('dados/dados_processados.csv')
        recomendacoes = recomendar_produtos(id_cliente, dados)
        
        # Limpa a caixa de resultados
        text_resultados.delete(1.0, tk.END)
        
        # Exibir recomendações
        if recomendacoes:
            for produto in recomendacoes:
                text_resultados.insert(tk.END, f"Produto ID: {produto}\n")
        else:
            text_resultados.insert(tk.END, "Nenhum produto recomendado.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um ID de cliente válido.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Sistema de Recomendação - TOTVS")

# Label e Entry para ID do Cliente
label_id_cliente = tk.Label(janela, text="ID do Cliente:")
label_id_cliente.pack()

entry_id_cliente = tk.Entry(janela)
entry_id_cliente.pack()

# Botão para obter recomendações
botao_recomendar = tk.Button(janela, text="Obter Recomendações", command=exibir_recomendacoes)
botao_recomendar.pack()

# Área de texto para exibir resultados
text_resultados = tk.Text(janela, height=10, width=50)
text_resultados.pack()

# Iniciar a aplicação
janela.mainloop()
