import pandas as pd
import numpy as np

class EmergyCalculator:
    
    # Aplica as regras da álgebra emergética sobre os dados do Inventário do Ciclo de Vida (LCI).
    

    def calculate_emergy(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calcula a emergia de cada linha multiplicando a Quantidade pela Transformidade (UEV).
        
        Parâmetros:
        df (pd.DataFrame): DataFrame contendo as colunas 'Quantidade' e 'Transformidade_UEV'.
        
        Retorna:
        pd.DataFrame: Um novo DataFrame com a coluna de resultados 'Emergia_seJ'.
        """
        # 1. Verificação de segurança: Garante que as colunas matemáticas existem
        required_cols = ['Quantidade', 'Transformidade_UEV']
        for col in required_cols:
            if col not in df.columns:
                raise ValueError(f"Erro no cálculo: A coluna obrigatória '{col}' não foi encontrada.")

        # 2. Cria uma cópia para não sobrescrever os dados originais brutos
        result_df = df.copy()


        # 3. O Cálculo da Álgebra Emergética (vetorizado com Pandas)

        # Substitui possíveis valores nulos ou vazios por 0 antes de multiplicar usando NumPy
        quantidade = np.where(result_df['Quantidade'].isna(), 0, result_df['Quantidade'])
        uev = np.where(result_df['Transformidade_UEV'].isna(), 0, result_df['Transformidade_UEV'])

        result_df['Emergia_seJ'] = quantidade * uev

        return result_df


    # Retorna a soma total da emergia do ecossistema/sistema.
    def get_total_emergy(self, df_calculated: pd.DataFrame) -> float:
    
        if 'Emergia_seJ' not in df_calculated.columns:
            raise ValueError("Você precisa rodar 'calculate_emergy' antes de pedir o total.")
            
        return df_calculated['Emergia_seJ'].sum()