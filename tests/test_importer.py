import pytest
import pandas as pd
from src.models.lci_importer import LCIImporter


def test_falha_leitura_arquivo_inexistente():
    importer = LCIImporter()
    with pytest.raises(FileNotFoundError):
        importer.load_data("data/arquivo_fantasma.xlsx")


def test_limpeza_matriz_converte_none_em_zero():
    importer = LCIImporter()
    df = pd.DataFrame({
        "Item": ["A", "B"],
        "Tipo": ["Insumo", "Insumo"],
        "Quantidade": [10, None],
        "Unidade": ["kg", "kg"],
        "Transformidade_UEV": [5, 7]
    })

    df_limpo = importer.clean_matrix(df)

    assert df_limpo["Quantidade"].iloc[1] == 0