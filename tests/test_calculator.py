import pytest
import pandas as pd
from src.models.emergy_calculator import EmergyCalculator


def test_calculo_multiplicacao_emergia():
    calc = EmergyCalculator()
    df = pd.DataFrame({
        "Quantidade": [10],
        "Transformidade_UEV": [5]
    })

    resultado = calc.calculate_emergy(df)

    assert resultado["Emergia_seJ"].iloc[0] == 50


def test_soma_total_emergia():
    calc = EmergyCalculator()
    df = pd.DataFrame({
        "Emergia_seJ": [50, 30]
    })

    total = calc.get_total_emergy(df)

    assert total == 80


def test_erro_sem_coluna_transformidade():
    calc = EmergyCalculator()
    df = pd.DataFrame({
        "Quantidade": [10]
    })

    with pytest.raises(ValueError):
        calc.calculate_emergy(df)