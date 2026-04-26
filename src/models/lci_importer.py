import pandas as pd
import os

# Importa e trata as matrizes de Inventário do Ciclo de Vida (LCI) para o cálculo de emergia.
class LCIImporter:
    
    def __init__(self):
        # Aqui podemos definir configurações iniciais se necessário no futuro
        pass

    def load_data(self, file_path: str) -> pd.DataFrame:
        # Lê um arquivo (CSV ou Excel) e retorna um DataFrame do Pandas.
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Erro: O arquivo '{file_path}' não foi encontrado.")

        # Verifica a extensão do arquivo para usar o método correto de leitura
        _, file_extension = os.path.splitext(file_path)
        
        try:
            if file_extension.lower() == '.csv':
                # Lê arquivos CSV
                df = pd.read_csv(file_path)
            elif file_extension.lower() in ['.xls', '.xlsx']:
                # Lê arquivos Excel (openpyxl)
                df = pd.read_excel(file_path)
            else:
                raise ValueError(f"Formato não suportado: {file_extension}. Use .csv ou .xlsx")
            
            # TODO: Adicionar lógica específica para limpar linhas/colunas vazias do LCI
            return df
            
        except Exception as e:
            raise Exception(f"Falha ao ler o arquivo de LCI: {str(e)}")

    def clean_matrix(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Método reservado para tratar matrizes específicas do SCALE no futuro.
        (ex: remover valores nulos, converter tipos, etc).
        """
        df_cleaned = df.fillna(0)
        return df_cleaned