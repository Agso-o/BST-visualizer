import sys
import BST  # Importa o arquivo BST.py que criamos na Etapa 1
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QPushButton, QMessageBox, QInputDialog, QLabel, QGridLayout
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

# --- Botão customizado para o Menu ---
# (Peguei seu `buttonMainMenu` e simplifiquei)
class MainMenuButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        FONT = QFont("Arial")
        FONT.setPixelSize(18)
        self.setFont(FONT)
        self.setFixedSize(350, 50)

# --- Janela Principal ---
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Instancia a Árvore Binária de Busca do nosso arquivo BST.py
        self.bst_manager = BST.bst()
        
        self.setWindowTitle("Visualizador de Árvore Binária de Busca (BST)")
        self.setFixedSize(500, 400) # Tamanho da janela
        
        # Define um widget central e um layout para ele
        self.central_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)
        
        # Inicia mostrando o menu principal
        self.showMainMenu()

    def showMainMenu(self):
        # Limpa o layout atual (caso esteja vindo de outra tela)
        self.clearLayout()
        
        # --- Cria os botões do menu ---
        
        # REQ #1: Adicionar elemento
        btn_add = MainMenuButton("1. Adicionar Elemento")
        btn_add.clicked.connect(self.adicionarElemento)

        # REQ #2: Plotar árvore
        btn_plot = MainMenuButton("2. Plotar Árvore (Altura <= 2)")
        btn_plot.clicked.connect(self.plotarArvore)
        
        # REQ #3, #4, #5: Informações
        btn_info = MainMenuButton("3. Mostrar Informações da Árvore")
        btn_info.clicked.connect(self.mostrarInformacoes)
        
        # REQ #6: Travessias
        btn_travessias = MainMenuButton("4. Mostrar Travessias")
        btn_travessias.clicked.connect(self.mostrarTravessias)
        
        # Sair
        btn_exit = MainMenuButton("Sair")
        btn_exit.clicked.connect(sys.exit)
  
        # --- Adiciona os botões ao layout ---
        self.main_layout.addWidget(btn_add, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(btn_plot, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(btn_info, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(btn_travessias, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addStretch() # Adiciona espaço flexível
        self.main_layout.addWidget(btn_exit, alignment=Qt.AlignmentFlag.AlignCenter)
  
    # --- Funções dos Botões ---

    def adicionarElemento(self):
        # Abre uma caixa de diálogo para pedir um número
        numero, ok = QInputDialog.getInt(self, 
                                          "Adicionar Elemento", 
                                          "Digite a chave (número natural):", 
                                          0, 0) # (título, label, valor_inicial, min)
        
        if ok:
            # Se o usuário clicou "OK", insere na árvore
            self.bst_manager.inserir(numero)
            QMessageBox.information(self, "Sucesso", f"Elemento '{numero}' inserido na árvore.")

    def plotarArvore(self):
        altura = self.bst_manager.altura()
        
        if altura > 2:
            QMessageBox.warning(self, "Erro ao Plotar", 
                                f"A árvore não pode ser plotada pois sua altura ({altura}) é maior que 2.")
            return

        # Se a altura é <= 2, busca os nós
        # O método plotar() retorna uma lista de 7 posições [0...6]
        nodes = self.bst_manager.plotar()
        
        # Converte 'None' para '---' para exibição
        display_nodes = [str(n) if n is not None else '---' for n in nodes]
        
        # Cria uma nova tela (widget) para mostrar a plotagem
        plot_widget = QWidget()
        plot_layout = QGridLayout()
        plot_layout.setSpacing(15)

        # Define fontes
        font_label = QFont("Arial", 12)
        font_node = QFont("Arial", 16, QFont.Weight.Bold)

        # --- Cria os QLabels para os 7 nós ---
        # (Esta é uma forma simples de "plotar" com texto)

        # Nível 0 (Raiz)
        lbl_raiz = QLabel(display_nodes[0])
        lbl_raiz.setFont(font_node)
        lbl_raiz.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Nível 1
        lbl_1_esq = QLabel(display_nodes[1])
        lbl_1_esq.setFont(font_node)
        lbl_1_esq.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        lbl_1_dir = QLabel(display_nodes[2])
        lbl_1_dir.setFont(font_node)
        lbl_1_dir.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Nível 2
        lbl_2_esq_esq = QLabel(display_nodes[3])
        lbl_2_esq_esq.setFont(font_node)
        lbl_2_esq_esq.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        lbl_2_esq_dir = QLabel(display_nodes[4])
        lbl_2_esq_dir.setFont(font_node)
        lbl_2_esq_dir.setAlignment(Qt.AlignmentFlag.AlignCenter)

        lbl_2_dir_esq = QLabel(display_nodes[5])
        lbl_2_dir_esq.setFont(font_node)
        lbl_2_dir_esq.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        lbl_2_dir_dir = QLabel(display_nodes[6])
        lbl_2_dir_dir.setFont(font_node)
        lbl_2_dir_dir.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # --- Adiciona os labels ao Grid Layout ---
        # (Linha, Coluna, LinSpan, ColSpan)
        
        # Nível 0
        plot_layout.addWidget(lbl_raiz, 0, 0, 1, 4) 
        
        # Linhas de conexão simples (opcional)
        plot_layout.addWidget(QLabel("╱", alignment=Qt.AlignmentFlag.AlignRight), 1, 0, 1, 2)
        plot_layout.addWidget(QLabel("╲", alignment=Qt.AlignmentFlag.AlignLeft), 1, 2, 1, 2)
        
        # Nível 1
        plot_layout.addWidget(lbl_1_esq, 2, 0, 1, 2)
        plot_layout.addWidget(lbl_1_dir, 2, 2, 1, 2)

        # Linhas de conexão
        plot_layout.addWidget(QLabel("╱"), 3, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        plot_layout.addWidget(QLabel("╲"), 3, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        plot_layout.addWidget(QLabel("╱"), 3, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        plot_layout.addWidget(QLabel("╲"), 3, 3, alignment=Qt.AlignmentFlag.AlignCenter)

        # Nível 2
        plot_layout.addWidget(lbl_2_esq_esq, 4, 0)
        plot_layout.addWidget(lbl_2_esq_dir, 4, 1)
        plot_layout.addWidget(lbl_2_dir_esq, 4, 2)
        plot_layout.addWidget(lbl_2_dir_dir, 4, 3)

        # Botão de voltar
        btn_back = QPushButton("Voltar ao Menu")
        btn_back.setFont(QFont("Arial", 12))
        btn_back.clicked.connect(self.showMainMenu)
        plot_layout.addWidget(btn_back, 5, 0, 1, 4)
        
        plot_widget.setLayout(plot_layout)
        
        # Substitui o widget central pelo widget de plotagem
        self.setCentralWidget(plot_widget)
        self.central_widget = plot_widget # Atualiza a referência


    def mostrarInformacoes(self):
        # Coleta todas as informações dos métodos da BST
        tamanho = self.bst_manager.tamanho()
        altura = self.bst_manager.altura()
        menor = self.bst_manager.menor()
        maior = self.bst_manager.maior()
        comprimento = self.bst_manager.internalPathLength()
        balanceada = self.bst_manager.balanceada()

        # Formata os dados para exibição
        info_str = f"""
        INFORMAÇÕES DA ÁRVORE:
        -----------------------------------
        Tamanho (Nº de Nós): {tamanho}
        Altura: {altura}
        -----------------------------------
        Menor Chave: {menor if menor is not None else 'N/A'}
        Maior Chave: {maior if maior is not None else 'N/A'}
        -----------------------------------
        Comprimento Interno: {comprimento}
        Está Balanceada (AVL)? {"Sim" if balanceada else "Não"}
        """
        
        QMessageBox.information(self, "Informações da Árvore", info_str)

    def mostrarTravessias(self):
        # Converte listas de números em strings formatadas
        def formatar(lista):
            if not lista:
                return "Árvore Vazia"
            return " -> ".join(map(str, lista))

        # Coleta as 4 travessias
        pre_ordem = self.bst_manager.preOrdem()
        em_ordem = self.bst_manager.emOrdem()
        pos_ordem = self.bst_manager.posOrdem()
        level_ordem = self.bst_manager.level()

        # Formata a string de saída
        info_str = f"""
        TRAVESSIAS DA ÁRVORE:
        
        Pré-Ordem (Raiz, Esq, Dir):
        {formatar(pre_ordem)}
        
        Em-Ordem (Esq, Raiz, Dir):
        {formatar(em_ordem)}
        
        Pós-Ordem (Esq, Dir, Raiz):
        {formatar(pos_ordem)}
        
        Em Largura (Por Nível):
        {formatar(level_ordem)}
        """
        
        # Usamos setDetailedText para uma mensagem grande e rolável
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle("Travessias da Árvore")
        msgBox.setText("Resultados das 4 travessias:")
        msgBox.setDetailedText(info_str)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.exec()


    def clearLayout(self):
        # Remove widgets do layout antigo antes de trocar de "tela"
        if self.main_layout is not None:
            while self.main_layout.count():
                item = self.main_layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
        
        # Se trocamos o widget central (como em plotarArvore)
        # precisamos criar um novo widget/layout
        if not isinstance(self.centralWidget(), QWidget) or self.centralWidget().layout() is None:
            self.central_widget = QWidget()
            self.main_layout = QVBoxLayout()
            self.central_widget.setLayout(self.main_layout)
            self.setCentralWidget(self.central_widget)

# --- Ponto de Entrada da Aplicação ---
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    
    myWindow = MyWindow() # Janela principal
    myWindow.show() # Exibe a janela principal
    
    sys.exit(app.exec()) # Inicia o loop da aplicação