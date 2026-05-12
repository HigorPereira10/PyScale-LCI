import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFileDialog, QTableWidget, QTableWidgetItem,
    QMessageBox, QHeaderView, QComboBox, QTabWidget, QProgressBar,
    QStackedWidget, QSpacerItem, QSizePolicy
)
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
import pyqtgraph as pg
import pandas as pd
from src.controllers.main_controller import MainController

class EmergyGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EcoVision - Cálculo de Emergia")
        self.setGeometry(300, 100, 1000, 700)
        
        self.df_result = None
        self.total_emergy = None
        self.indices = None
        self.bar_color = '#89b4fa' 

        self.controller = MainController()

        # O StackedWidget gerencia as múltiplas telas do nosso app
        self.stacked_widget = QStackedWidget()
        
        # Layout raiz da janela
        root_layout = QVBoxLayout()
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.addWidget(self.stacked_widget)
        self.setLayout(root_layout)

        # Inicializa as duas telas
        self.init_welcome_screen()
        self.init_main_screen()

        self.apply_theme("Dark Mode")
        
        # Inicia a animação de Fade In
        self.play_fade_in()

    # =======================
    # TELA DE BOAS-VINDAS 
    # =======================

    def init_welcome_screen(self):
        self.welcome_widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Espaçador superior
        layout.addSpacerItem(QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Título principal com fonte serifada e cor acetinada
        self.lbl_title = QLabel("EcoVision")
        self.lbl_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_title.setStyleSheet("""
            font-family: 'Georgia', 'Times New Roman', serif;
            font-size: 72px;
            font-weight: bold;
            color: #d4af37; /* Dourado Acetinado */
            letter-spacing: 2px;
        """)
        layout.addWidget(self.lbl_title)

        # Subtítulo
        self.lbl_subtitle = QLabel("Cálculo de Emergia Avançado")
        self.lbl_subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_subtitle.setStyleSheet("""
            font-family: 'Segoe UI', Arial;
            font-size: 24px;
            color: #a6adc8;
            margin-bottom: 40px;
        """)
        layout.addWidget(self.lbl_subtitle)

        # Botões da tela inicial
        buttons_layout = QHBoxLayout()
        buttons_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        buttons_layout.setSpacing(20)

        self.btn_get_started = QPushButton("Get Started")
        self.btn_get_started.setFixedWidth(200)
        self.btn_get_started.setStyleSheet("""
            QPushButton {
                background-color: #d4af37;
                color: #11111b;
                font-size: 16px;
                padding: 12px;
                border-radius: 8px;
            }
            QPushButton:hover { background-color: #f3c746; }
        """)
        self.btn_get_started.clicked.connect(self.go_to_main_screen)

        self.btn_info = QPushButton("O que é Cálculo de Emergia?")
        self.btn_info.setFixedWidth(250)
        self.btn_info.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #cdd6f4;
                font-size: 16px;
                padding: 12px;
                border: 1px solid #cdd6f4;
                border-radius: 8px;
            }
            QPushButton:hover { background-color: #313244; }
        """)
        self.btn_info.clicked.connect(self.show_emergy_info)

        buttons_layout.addWidget(self.btn_get_started)
        buttons_layout.addWidget(self.btn_info)
        layout.addLayout(buttons_layout)

        # Espaçador inferior
        layout.addSpacerItem(QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.welcome_widget.setLayout(layout)
        self.stacked_widget.addWidget(self.welcome_widget)

    def play_fade_in(self):
        # Opacidade começa em 0
        self.setWindowOpacity(0.0)
        
        # Animação da propriedade windowOpacity
        self.fade_anim = QPropertyAnimation(self, b"windowOpacity")
        self.fade_anim.setDuration(1500) # 1.5 segundos
        self.fade_anim.setStartValue(0.0)
        self.fade_anim.setEndValue(1.0)
        self.fade_anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.fade_anim.start()

    def go_to_main_screen(self):
        # Muda a tela visível para o índice 1 (Interface de Cálculos)
        self.stacked_widget.setCurrentIndex(1)

    def show_emergy_info(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("O que é Cálculo de Emergia?")
        msg.setIcon(QMessageBox.Icon.Information)
        
        # Estilização do Container do Pop-up via CSS, pq O QMessageBox tem algumas limitações chatas com o HTML.
        # Aqui garantimos que o fundo seja escuro e a cor base do texto seja branca
        msg.setStyleSheet("""
            QMessageBox {
                background-color: #1e1e2e;
            }
            QLabel {
                color: #ffffff; /* Cor padrão para todo o texto */
                min-width: 500px; /* Aumentado para o texto não ficar espremido */
            }
            QPushButton {
                background-color: #d4af37;
                color: #11111b;
                font-weight: bold;
                padding: 10px 25px;
                border-radius: 6px;
                font-size: 16px;
                margin-top: 15px;
            }
        """)

        # Parte 1: Título em Branco, 26px, Serifado
        # <span> para evitar que o <h2> force margens estranhas
        titulo_html = (
            "<span style='color: #ffffff; font-size: 19px; font-family: Segoe UI, sans-serif; font-weight: bold;'>"
            "O Cálculo de Emergia é uma metodologia de contabilidade ambiental e termodinâmica"
            "desenvolvida por H.T. Odum.</span>"
        )
        msg.setText(titulo_html)
        
        corpo_html = (
            "<div style='color: #e0e0e0; font-size: 19px; line-height: 140%; font-family: Segoe UI, sans-serif;'>"
            "A emergia expressa todos os recursos (luz solar, vento, combustíveis e mão de obra) "
            "em uma única unidade comum: o <b>Joule Equivalente Solar (seJ)</b>.<br><br>"
            "No EcoVision, esse cálculo permite que você entenda quanto de 'trabalho da natureza' "
            "foi necessário para sustentar seu processo produtivo, revelando a <b>verdadeira sustentabilidade</b> "
            "além dos custos financeiros.</div>"
        )
        msg.setInformativeText(corpo_html)

        # Aplica um estilo rápido ao pop-up para não ficar branco no dark mode
        if self.theme_combo.currentText() == "Dark Mode":
            msg.setStyleSheet("QMessageBox { background-color: #1e1e2e; color: #cdd6f4; } QLabel { color: #cdd6f4; } QPushButton { background-color: #313244; color: white; padding: 5px 15px; }")
        msg.exec()


    # ==========================================
    # INTERFACE PRINCIPAL (ANTIGO INIT_UI)
    # ==========================================

    def init_main_screen(self):
        self.main_app_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(25, 25, 25, 25)
        main_layout.setSpacing(15)

        # 🟢 Seção Superior
        top_layout = QHBoxLayout()
        self.label_file = QLabel("Nenhum arquivo selecionado")
        self.label_file.setStyleSheet("font-style: italic;")
        
        btn_browse = QPushButton("📁 Carregar Matriz LCI")
        btn_browse.clicked.connect(self.browse_file)
        
        btn_run = QPushButton("▶️ Rodar Simulação")
        btn_run.clicked.connect(self.run_simulation)
        
        btn_clear = QPushButton("🗑️ Nova Simulação")
        btn_clear.clicked.connect(self.clear_simulation)
        
        lbl_theme = QLabel("Tema:")
        lbl_theme.setStyleSheet("font-weight: bold;")
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Dark Mode", "Light Mode"])
        self.theme_combo.currentTextChanged.connect(self.apply_theme)
        
        top_layout.addWidget(btn_browse)
        top_layout.addWidget(self.label_file, stretch=1)
        top_layout.addWidget(btn_run)
        top_layout.addWidget(btn_clear)
        top_layout.addSpacing(20)
        top_layout.addWidget(lbl_theme)
        top_layout.addWidget(self.theme_combo)
        main_layout.addLayout(top_layout)

        # 🟢 Sistema de Guias
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs, stretch=4)

        # --- GUIA 1 ---
        self.tab1 = QWidget()
        tab1_layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setVisible(False)
        tab1_layout.addWidget(self.table, stretch=3)

        results_layout = QHBoxLayout()
        self.label_total = QLabel("Total Emergia: ---")
        self.label_total.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_total.setStyleSheet("font-size: 20px; font-weight: bold;")
        results_layout.addWidget(self.label_total)

        self.plot_widget = pg.PlotWidget()
        self.plot_widget.showGrid(x=True, y=True, alpha=0.3)
        self.plot_widget.setLabel('left', 'Emergia (seJ)')
        self.plot_widget.setLabel('bottom', 'Itens do LCI')
        results_layout.addWidget(self.plot_widget, stretch=2)

        tab1_layout.addLayout(results_layout, stretch=2)
        self.tab1.setLayout(tab1_layout)
        self.tabs.addTab(self.tab1, "📊 Dados e Tabela LCI")

        # --- GUIA 2 ---
        self.tab2 = QWidget()
        tab2_layout = QVBoxLayout()
        self.label_indices = QLabel("Aguardando simulação...\n(Certifique-se de que a planilha possui a coluna 'Categoria' com R, N ou F)")
        self.label_indices.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_indices.setStyleSheet("font-size: 16px; margin: 20px;")
        tab2_layout.addWidget(self.label_indices)

        self.plot_categories = pg.PlotWidget()
        self.plot_categories.showGrid(x=True, y=True, alpha=0.3)
        self.plot_categories.setLabel('left', 'Emergia (seJ)')
        self.plot_categories.setLabel('bottom', 'Categorias Emergéticas')
        ticks = [[(0, 'R (Renovável)'), (1, 'N (Não-Renov.)'), (2, 'F (Economia)')]]
        self.plot_categories.getAxis('bottom').setTicks(ticks)
        
        tab2_layout.addWidget(self.plot_categories, stretch=1)
        self.tab2.setLayout(tab2_layout)
        self.tabs.addTab(self.tab2, "📈 Análise Avançada (R, N, F)")

        # 🟢 Botões de Exportação
        export_layout = QHBoxLayout()
        self.btn_export_table = QPushButton("💾 Exportar Tabela")
        self.btn_export_table.clicked.connect(self.export_table)
        self.btn_export_table.setEnabled(False) 
        
        self.btn_export_graph = QPushButton("📊 Exportar Gráficos")
        self.btn_export_graph.clicked.connect(self.export_graph)
        self.btn_export_graph.setEnabled(False) 
        
        export_layout.addWidget(self.btn_export_table)
        export_layout.addWidget(self.btn_export_graph)
        main_layout.addLayout(export_layout)

        # 🟢 Barra de Progresso e Logs
        footer_layout = QHBoxLayout()
        self.label_logs = QLabel("Status: Aguardando arquivo...")
        self.label_logs.setStyleSheet("font-style: italic;")
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setFixedWidth(300) 
        
        footer_layout.addWidget(self.label_logs)
        footer_layout.addWidget(self.progress_bar)
        main_layout.addLayout(footer_layout)

        self.main_app_widget.setLayout(main_layout)
        self.stacked_widget.addWidget(self.main_app_widget)

    # ===== Funções de Estilização =====
    def apply_theme(self, theme_name):
        base_style = "font-family: 'Segoe UI', Arial; font-size: 14px;"
        
        if theme_name == "Dark Mode":
            # Estilo que afeta APENAS os widgets dentro da tela principal para não quebrar a tela de boas vindas
            self.main_app_widget.setStyleSheet(f"""
                QWidget {{ background-color: #11111b; color: #cdd6f4; {base_style} }}
                QPushButton {{ background-color: #89b4fa; color: #11111b; border-radius: 6px; padding: 10px; font-weight: bold; }}
                QPushButton:hover {{ background-color: #b4befe; }}
                QPushButton:disabled {{ background-color: #313244; color: #6c7086; }}
                QTableWidget {{ background-color: #1e1e2e; alternate-background-color: #181825; border: 1px solid #313244; border-radius: 6px; }}
                QHeaderView::section {{ background-color: #313244; color: #cdd6f4; padding: 6px; border: none; font-weight: bold; }}
                QComboBox {{ background-color: #1e1e2e; border: 1px solid #313244; border-radius: 4px; padding: 4px; }}
                QTabWidget::pane {{ border: 1px solid #313244; border-radius: 6px; }}
                QTabBar::tab {{ background: #181825; color: #cdd6f4; padding: 10px 20px; border-top-left-radius: 6px; border-top-right-radius: 6px; margin-right: 2px; }}
                QTabBar::tab:selected {{ background: #89b4fa; color: #11111b; font-weight: bold; }}
                QProgressBar {{ border: 1px solid #313244; border-radius: 4px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; }}
                QProgressBar::chunk {{ background-color: #89b4fa; border-radius: 3px; }}
            """)
            # Mantém o fundo da janela inteiro escuro
            self.setStyleSheet("background-color: #11111b;")
            self.bar_color = '#89b4fa'
            self._set_graph_theme('#1e1e2e', '#cdd6f4')

        else:
            self.main_app_widget.setStyleSheet(f"""
                QWidget {{ background-color: #f8f9fa; color: #212529; {base_style} }}
                QPushButton {{ background-color: #0d6efd; color: #ffffff; border-radius: 6px; padding: 10px; font-weight: bold; }}
                QPushButton:hover {{ background-color: #0b5ed7; }}
                QPushButton:disabled {{ background-color: #e9ecef; color: #adb5bd; }}
                QTableWidget {{ background-color: #ffffff; alternate-background-color: #f1f3f5; border: 1px solid #dee2e6; border-radius: 6px; }}
                QHeaderView::section {{ background-color: #e9ecef; color: #495057; padding: 6px; border: none; font-weight: bold; }}
                QComboBox {{ background-color: #ffffff; border: 1px solid #ced4da; border-radius: 4px; padding: 4px; }}
                QTabWidget::pane {{ border: 1px solid #dee2e6; border-radius: 6px; }}
                QTabBar::tab {{ background: #e9ecef; color: #495057; padding: 10px 20px; border-top-left-radius: 6px; border-top-right-radius: 6px; margin-right: 2px; }}
                QTabBar::tab:selected {{ background: #0d6efd; color: #ffffff; font-weight: bold; }}
                QProgressBar {{ border: 1px solid #dee2e6; border-radius: 4px; text-align: center; color: #212529; background-color: #ffffff; }}
                QProgressBar::chunk {{ background-color: #0d6efd; border-radius: 3px; }}
            """)
            self.setStyleSheet("background-color: #f8f9fa;")
            self.bar_color = '#0d6efd'
            self._set_graph_theme('#ffffff', '#495057')

        self.update_table()
        self.update_plot()
        self.update_advanced_tab()

    def _set_graph_theme(self, bg_color, fg_color):
        for plot in [self.plot_widget, self.plot_categories]:
            plot.setBackground(bg_color)
            plot.getAxis('left').setPen(fg_color)
            plot.getAxis('bottom').setPen(fg_color)
            plot.getAxis('left').setTextPen(fg_color)
            plot.getAxis('bottom').setTextPen(fg_color)

    # ===== Funções de Lógica =====
    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecione arquivo LCI", "", "Arquivos CSV (*.csv);;Excel (*.xls *.xlsx)")
        if file_path:
            self.label_file.setText(file_path)
            self.label_logs.setText("Arquivo selecionado com sucesso ✅")
            self.progress_bar.setValue(0)

    def clear_simulation(self):
        self.df_result = None
        self.total_emergy = None
        self.indices = None
        
        self.label_file.setText("Nenhum arquivo selecionado")
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        self.plot_widget.clear()
        self.plot_categories.clear()
        
        self.label_total.setText("Total Emergia: ---")
        self.label_indices.setText("Aguardando simulação...\n(Certifique-se de que a planilha possui a coluna 'Categoria' com R, N ou F)")
        
        self.btn_export_table.setEnabled(False)
        self.btn_export_graph.setEnabled(False)
        
        self.progress_bar.setValue(0)
        self.label_logs.setText("Status: Nova simulação. Aguardando matriz LCI...")

    def run_simulation(self):
        file_path = self.label_file.text()
        if file_path == "Nenhum arquivo selecionado":
            QMessageBox.warning(self, "Aviso", "Selecione um arquivo LCI primeiro!")
            return

        self.label_logs.setText("Lendo matriz LCI e calculando emergia... 🔄")
        self.progress_bar.setValue(20)
        QApplication.processEvents()

        final_data, total_emergy, indices = self.controller.run_simulation(file_path)

        if final_data is not None:
            if 'Categoria' not in final_data.columns:
                final_data.insert(0, 'Categoria', "")

            self.df_result = final_data
            self.total_emergy = total_emergy
            self.indices = indices

            self.progress_bar.setValue(60)
            self.label_logs.setText("Gerando tabela e verificando erros... 🔄")
            QApplication.processEvents()

            self.update_table()
            self.label_total.setText(f"Total Emergia:\n{total_emergy:,.2f} SeJ")
            
            self.progress_bar.setValue(85)
            self.label_logs.setText("Desenhando gráficos... 🔄")
            QApplication.processEvents()

            self.update_plot()
            self.update_advanced_tab()
            
            self.btn_export_table.setEnabled(True)
            self.btn_export_graph.setEnabled(True)
            
            self.progress_bar.setValue(100)
            self.label_logs.setText("Simulação concluída com sucesso ✅")
        else:
            self.progress_bar.setValue(0)
            QMessageBox.critical(self, "Erro na simulação", "Erro! Verifique o console ou a formatação do arquivo.")
            self.label_logs.setText("Erro na simulação ❌")

    def update_table(self):
        if self.df_result is not None:
            self.table.setRowCount(len(self.df_result))
            self.table.setColumnCount(len(self.df_result.columns))
            self.table.setHorizontalHeaderLabels(self.df_result.columns.tolist())
            self.table.setAlternatingRowColors(True)

            is_dark = self.theme_combo.currentText() == "Dark Mode"
            alert_color = QColor('#5c1e24') if is_dark else QColor('#fff3cd')

            for i, row in self.df_result.iterrows():
                has_error = False
                if 'Transformidade_UEV' in self.df_result.columns:
                    val = row['Transformidade_UEV']
                    if pd.isna(val) or val == 0 or str(val).strip() == '':
                        has_error = True

                for j, col in enumerate(self.df_result.columns):
                    item = QTableWidgetItem(str(row[col]))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    
                    if has_error:
                        item.setBackground(alert_color)
                        
                    self.table.setItem(i, j, item)

    def update_plot(self):
        if self.df_result is not None:
            self.plot_widget.clear()
            y = self.df_result['Emergia_seJ'].values
            x = list(range(len(y)))
            bar_graph = pg.BarGraphItem(x=x, height=y, width=0.6, brush=self.bar_color)
            self.plot_widget.addItem(bar_graph)

    def update_advanced_tab(self):
        if self.indices is not None:
            texto_indices = (
                f"<b>Índices Emergéticos Calculados:</b><br><br>"
                f"🌱 Renovável (R): {self.indices['R']:,.2f} seJ<br>"
                f"🛢️ Não-Renovável (N): {self.indices['N']:,.2f} seJ<br>"
                f"🏭 Economia (F): {self.indices['F']:,.2f} seJ<br><br>"
                f"📊 <b>EYR</b> (Razão de Rendimento): <span style='color:{self.bar_color};'>{self.indices['EYR']:.2f}</span><br>"
                f"⚠️ <b>EIR</b> (Carga Ambiental): <span style='color:{self.bar_color};'>{self.indices['EIR']:.2f}</span>"
            )
            self.label_indices.setText(texto_indices)

            self.plot_categories.clear()
            y_cat = [self.indices['R'], self.indices['N'], self.indices['F']]
            x_cat = [0, 1, 2] 
            
            brushes = ['#a6e3a1', '#f38ba8', '#f9e2af'] if self.theme_combo.currentText() == "Dark Mode" else ['#198754', '#dc3545', '#ffc107']
            
            for i in range(3):
                bar = pg.BarGraphItem(x=[x_cat[i]], height=[y_cat[i]], width=0.5, brush=brushes[i])
                self.plot_categories.addItem(bar)
        
        elif self.df_result is not None:
             self.label_indices.setText("Matriz calculada, mas a coluna <b>'Categoria'</b> (R, N, F) não foi preenchida.\nEdite o arquivo e rode novamente para ver os índices.")
             self.plot_categories.clear()

    # ===== Funções de Exportação =====
    def export_table(self):
        if self.df_result is None: return
        file_path, _ = QFileDialog.getSaveFileName(self, "Salvar Tabela", "resultados_emergia.xlsx", "Excel (*.xlsx);;CSV (*.csv)")
        if file_path:
            try:
                if file_path.endswith('.xlsx'): self.df_result.to_excel(file_path, index=False)
                else: self.df_result.to_csv(file_path, index=False, sep=';')
                self.label_logs.setText(f"Tabela exportada com sucesso: {file_path} 💾✅")
            except Exception as e:
                QMessageBox.critical(self, "Erro ao Exportar", str(e))

    def export_graph(self):
        if self.df_result is None: return
        file_path, _ = QFileDialog.getSaveFileName(self, "Salvar Gráficos", "graficos_emergia.png", "Imagem PNG (*.png)")
        if file_path:
            try:
                if self.tabs.currentIndex() == 0:
                    pixmap = self.plot_widget.grab()
                else:
                    pixmap = self.plot_categories.grab()
                pixmap.save(file_path, "PNG")
                self.label_logs.setText(f"Gráfico exportado com sucesso: {file_path} 📊✅")
            except Exception as e:
                QMessageBox.critical(self, "Erro ao Exportar", str(e))