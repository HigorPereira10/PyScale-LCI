import pandas as pd
import os

print("⏳ [Checkpoint 1] Iniciando a montagem dos dados de teste...")

try:
    # Dados simulados de um inventário agrícola
    dados_lci = {
        "Item": [
            "Luz Solar", "Chuva", "Vento", "Perda de Solo", 
            "Fertilizante NPK", "Sementes", "Combustível Trator", 
            "Defensivo Agrícola", "Mão de Obra"
        ],
        "Categoria": ["R", "R", "R", "N", "F", "F", "N", "F", "F"],
        "Quantidade": [
            1.5e10, 5.2e8, 1.1e8, 5.0e4, 
            200.0, 50.0, 120.0, 15.0, 300.0
        ],
        "Transformidade_UEV": [
            1.0, 3.05e4, 1.50e3, 7.40e4, 
            4.50e9, 1.20e9, 6.60e4, 
            0.0,  # ERRO PROPOSITAL para testar o alerta visual!
            8.20e6
        ],
        "Unidade": ["J", "J", "J", "g", "g", "g", "J", "g", "h"]
    }

    df_teste = pd.DataFrame(dados_lci)
    print("✅ [Checkpoint 2] Tabela montada na memória com sucesso.")

    # Definindo o nome do arquivo e o caminho absoluto
    nome_arquivo = "matriz_teste_agricola.xlsx"
    caminho_completo = os.path.abspath(nome_arquivo)

    print("⏳ [Checkpoint 3] Tentando salvar o arquivo Excel...")
    
    # Exporta para Excel
    df_teste.to_excel(caminho_completo, index=False)

    print("\n🎉 SALVO COM SUCESSSO! ")
    print(f"👉 O arquivo foi salvo neste local:\n{caminho_completo}\n")

except PermissionError:
    print("\n❌ ERRO DE PERMISSÃO: O arquivo já existe e está aberto no Excel!")
    print("👉 Feche o Excel e rode o script novamente.")
except Exception as e:
    print(f"\n❌ ERRO INESPERADO no [Checkpoint 3]: {str(e)}")