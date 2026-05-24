from src.models.lci_importer import LCIImporter
from src.models.emergy_calculator import EmergyCalculator

class MainController:
    
    # Faz a ponte entre os Modelos (dados/cálculos) e a Interface Gráfica (View).

    def __init__(self):
        self.importer = LCIImporter()
        self.calculator = EmergyCalculator()

    def run_simulation(self, file_path: str):
        # Lê o arquivo, limpa e calcula.
        
        try:
            print(f"🔄 Iniciando simulação para: {file_path}")
            
            # Importar e limpar
            raw_data = self.importer.load_data(file_path)
            clean_data = self.importer.clean_matrix(raw_data)
            
            # Calcular a emergia básica
            final_data = self.calculator.calculate_emergy(clean_data)
            total_emergy = self.calculator.get_total_emergy(final_data)
            
            # Calcular os Índices Avançados
            # Se não tiver a coluna, isso aqui vai guardar 'None', mas o programa continua!
            indices = self.calculator.calculate_indices(final_data)
            
            # Retornar todos os resultados para quem pediu (Interface Visual)
            return final_data, total_emergy, indices
            
        except Exception as e:
            print(f"❌ Erro na simulação: {e}")
            # Como agora retorna 3 coisas, retorna 3 'Nones' no erro
            return None, None, None