import os
from src.controllers.main_controller import MainController

def main():
    print("="*40)
    print(" SISTEMA PyScale-LCI - Backend v1.0")
    print("="*40)
    
    # Define o caminho do arquivo de teste
    arquivo_lci = os.path.abspath(os.path.join("data", "sample_lci.xlsx"))
    
    # Inicia o Controlador
    app = MainController()
    
    # Roda a simulação completa
    resultados_df, total = app.run_simulation(arquivo_lci)
    
    if resultados_df is not None:
        print("\n📊 RESULTADOS DO CÁLCULO EMERGÉTICO:")
        print(resultados_df[['Item', 'Tipo', 'Emergia_seJ']])
        print("-" * 40)
        print(f"🌍 EMERGIA TOTAL DO SISTEMA: {total:.2e} seJ")
        print("=" * 40)

if __name__ == "__main__":
    main()