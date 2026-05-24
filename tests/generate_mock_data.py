import pandas as pd
import os
import sys 
# Descobre onde este arquivo está e sobe um nível para a raiz do projeto
raiz_do_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_do_projeto)
from src.models.lci_importer import LCIImporter



# Cria um arquivo Excel fictício simulando um Inventário do Ciclo de Vida (LCI) simples.
def create_mock_lci_file():
    
    # Garante que a pasta 'data' existe
    os.makedirs('data', exist_ok=True)
    file_path = 'data/sample_lci.xlsx'
    
    # Criando uma tabela fictícia (ex: produção agrícola básica)
    dados = {
        "Item": ["Energia Solar", "Chuva", "Fertilizante", "Trator", "Sementes"],
        "Tipo": ["Natureza", "Natureza", "Insumo", "Insumo", "Insumo"],
        "Quantidade": [15000.0, 5000.0, 250.0, 1.5, 30.0],
        "Unidade": ["J", "g", "g", "kg", "g"],
        "Transformidade_UEV": [1.0, 3.1e4, 4.0e9, 3.4e9, 1.2e5] # Valores fictícios
    }
    
    # Transforma o dicionário em um DataFrame e salva como Excel
    df = pd.DataFrame(dados)
    df.to_excel(file_path, index=False)
    print(f"✅ Arquivo de teste gerado com sucesso em: {file_path}")
    
    return file_path

def main():
    print("--- Iniciando o Sistema PyScale-LCI ---")
    
    # Cria o arquivo falso
    arquivo_teste = create_mock_lci_file()
    
    # Instancia o importador
    importer = LCIImporter()
    
    print("\n--- Testando a leitura da Planilha ---")
    try:
        # Lê e limpa os dados
        dados_brutos = importer.load_data(arquivo_teste)
        dados_limpos = importer.clean_matrix(dados_brutos)
        
        # Exibe as 5 primeiras linhas no terminal
        print(dados_limpos.head())
        print("\n✅ Leitura concluída com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro durante o teste: {e}")

if __name__ == "__main__":
    main()