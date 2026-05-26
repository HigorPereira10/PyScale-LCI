readme_content = """# PyScale-LCI ♻️

O **PyScale-LCI** é uma aplicação desktop desenvolvida em Python para a realização de **Cálculos Emergéticos** estruturados a partir de matrizes de **Inventários de Ciclo de Vida (LCI)**. O projeto é inspirado no software científico *SCALE* (Marvuglia et al., 2013) e foi concebido como parte das Atividades Práticas Supervisionadas (APS) de Engenharia de Software da Universidade Paulista (UNIP).

O sistema provê uma infraestrutura matemática vetorizada e uma interface gráfica fluida para engenharia ecológica, permitindo a contabilidade da energia incorporada (direta e indiretamente) em sistemas produtivos — utilizando como estudo de caso um inventário real de **Produção de Tomates em Estufa**.

---

## 📌 Funcionalidades Principais

* **Importação e Higienização de LCI:** Leitura automatizada de planilhas eletrônicas (Microsoft Excel `.xlsx` e `.csv`) utilizando a biblioteca *Pandas*.
* **Tratamento de Inconsistências (Tolerância a Falhas):** Arquitetura segura que intercepta cabeçalhos corrompidos, previne falhas em cascata retornando instâncias nulas de controle e injeta dinamicamente dados secundários ausentes.
* **Motor de Cálculo Emergético:** Multiplicação matricial vetorizada de fluxos físicos reais (`Quantidade`) pelas suas respectivas escalas termodinâmicas (`Transformidade_UEV`) para a obtenção da Emergia Total em *Solar Emjoules* (sej).
* **Análise de Sustentabilidade Avançada:** Segregação automática de fluxos de insumos por indexadores metodológicos:
    * **R** (Recursos Renováveis da Natureza)
    * **N** (Recursos Não-Renováveis)
    * **F** (Insumos Adquiridos da Economia / Feedbacks)
* **Geração de Macroindicadores Ecológicos:** Cálculo instantâneo dos índices **EYR** (*Emergy Yield Ratio* / Razão de Rendimento Emergético) e **EIR** (*Emergy Investment Ratio* / Razão de Investimento Emergético).
* **Interface Gráfica de Usuário (UX/UI):** Interface reativa construída sobre o framework *PyQt6*, com sistema de transição de telas por pilha (*QStackedWidget*), barras de progresso animadas e tabelas interativas com rotinas de controle de qualidade visual (células com valores inconsistentes ou zerados são destacadas automaticamente em cores de alerta).
* **Visualização Dinâmica de Dados:** Renderização em tempo real de gráficos de barras dos fluxos de emergia por meio da biblioteca de alta performance *PyQtGraph*.
* **Exportação de Resultados:** Salvamento dos dados computados e relatórios consolidados de volta para formatos `.xlsx` (Excel) e `.csv`.

---

## 📐 Arquitetura do Sistema (Padrão MVC)

O projeto foi edificado seguindo rigorosamente o padrão arquitetural **Model-View-Controller (MVC)**, garantindo a separação de conceitos, modularidade e alta testabilidade.

```text
PyScale-LCI/
│
├── data/                      # Arquivos de dados e inventários (Ex: Tomate em Estufa)
│
├── src/                       # Código-fonte principal da aplicação
│   ├── controllers/           # Camada Controller (Orquestração de fluxo)
│   │   └── main_controller.py
│   │
│   ├── models/                # Camada Model (Regras de negócio e Matemática Pura)
│   │   ├── emergy_calculator.py
│   │   └── lci_importer.py
│   │
│   └── views/                 # Camada View (Interface Gráfica PyQt6)
│       └── gui.py
│
├── tests/                     # Suíte de Testes Automatizados e QA
│   ├── test_calculator.py     # Testes das equações matemáticas e matrizes
│   ├── test_importer.py       # Testes de validação de leitura do Excel
│   └── gerar_teste.py         # Script utilitário para geração de massa de dados sintéticos
│
├── .gitignore                 # Filtro de arquivos locais e cache do ambiente
├── pytest.ini                 # Configuração de caminhos do framework Pytest
├── requirements.txt           # Gerenciador de dependências e bibliotecas do projeto
├── main.py                    # Ponto de entrada (Bootstrap) da aplicação
└── README.md                  # Documentação do repositório

## Divisão de Responsabilidades:
* **Model (src/models/):** Isolada de qualquer elemento visual. Contém a lógica pura da álgebra emergética e funções de manipulação de matrizes de dados.

* **View (src/views/):** Camada de apresentação. Renderiza componentes de tela e escuta ações do usuário. Não processa regras de cálculo.

* **Controller (src/controllers/):** Intermediário reativo. Intercepta os eventos da View, aciona os métodos analíticos da Model e devolve os dados estruturados para atualização da interface.


## 🛠️ Tecnologias e Dependências
O ecossistema do projeto utiliza as seguintes tecnologias em nível de produção:

* Python 3.13+ (Linguagem base do ecossistema)

* PyQt6 (Construção da interface gráfica nativa de alta fidelidade)

* PyQtGraph (Plotagem gráfica vetorial de altíssima velocidade e interatividade)

* Pandas (Estruturação de dados em DataFrames e processamento matricial)

* Openpyxl (Mecanismo de leitura e gravação assíncrona de arquivos .xlsx)

* Pytest (Framework de automação de testes unitários e asserções de QA)

