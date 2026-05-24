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
        # Verificação de segurança: Garante que as colunas matemáticas existem
        required_cols = ['Quantidade', 'Transformidade_UEV']
        for col in required_cols:
            if col not in df.columns:
                raise ValueError(f"Erro no cálculo: A coluna obrigatória '{col}' não foi encontrada.")

        # Cria uma cópia para não sobrescrever os dados originais brutos
        result_df = df.copy()

        # O Cálculo da Álgebra Emergética (vetorizado com Pandas)
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

    # lógica de "tolerância a falhas": 
    # se a coluna Categoria não existir Excel/CSV, o sistema cria automaticamente uma coluna vazia na tabela, fazendo com que o programa rode normalmente

    def calculate_indices(self, df_calculated: pd.DataFrame) -> dict:
        """
        Calcula os índices emergéticos padrão (EYR, EIR) baseado nas categorias R, N e F.
        Se a coluna 'Categoria' não existir, retorna None sem quebrar o sistema.
        """
        # A exceção entra aqui:
        if 'Categoria' not in df_calculated.columns:
            return None

        # Agrupa e soma a emergia por categoria
        grouped = df_calculated.groupby('Categoria')['Emergia_seJ'].sum()
        
        # Extrai os valores (com fallback para 0 caso a categoria não tenha sido usada)
        R = grouped.get('R', 0.0)
        N = grouped.get('N', 0.0)
        F = grouped.get('F', 0.0)
        
        Y = R + N + F
        
        # Evita divisão por zero caso a matriz esteja incompleta
        EYR = (Y / F) if F > 0 else 0.0
        EIR = ((F + N) / R) if R > 0 else 0.0
        
        return {
            'R': R,
            'N': N,
            'F': F,
            'Y': Y,
            'EYR': EYR,
            'EIR': EIR
        }