# Cria de fato a interface da aplicacao
# Para futuras modificacao, e interessante implementar um esquema de navegacao usando QStackedWidget
from PySide6.QtWidgets import QMainWindow, QWidget, QMessageBox, QInputDialog, QCheckBox, QListWidget, QStyle # Principais widgets
from PySide6.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt
from .smallWidgets import inputValue, messageDialog, buttonMainMenu
from GUIs.constants import ICON2_PATH, WINDOW_HEIGTH, WINDOW_WIDTH
import BST
from GUIs.TreePlotter import PlotWindow
import sys

  
# Herda QMainWindow para ter acesso a alguns componentes da janela em si, como title e icon 
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.errorMessage = None # Gerencia a messagem de erro na leitura de dado, se ela deve ser exibida ou nao
        self.bst_manager = BST.bst()
        self.plot_window = None
        self.setWindowTitle("Àrvore binária de busca")
        self.setFixedSize(WINDOW_HEIGTH, WINDOW_WIDTH)
        self.setWindowIcon(QIcon(ICON2_PATH)) # Troca o icone da janela
        self.showMainMenu()  # Mostra a primeira janela
  
  
    # Renderiza o menu principal da aplicacao 
    def showMainMenu(self):
        CENTER = Qt.AlignmentFlag.AlignCenter # Cria um centralizacao 
  
        widget = QWidget() # Widget generico
        layout = QVBoxLayout() # Box vertical 
  
        # Adiciona um elemento na BST
        button_add_element = buttonMainMenu("Adicionar elemento")
        button_add_element.clicked.connect(self.adicionarElemento) # Adiciona funcao para esse botao

        # Mostra o desenho da árvore
        button_plot_drawn = buttonMainMenu("Plotar o desenho da árvore")
        button_plot_drawn.clicked.connect(self.plotarArvore) # Adiciona funcao para esse botao
        
        # informações sobre a árvore
        button_bst_info = buttonMainMenu("Mostrar informações sobre a árvore")
        button_bst_info.clicked.connect(self.mostrarInformacoes) # Adiciona funcao para esse botao
        
        # Vizualia as travessias
        button_view_queue = buttonMainMenu("Mostrar travessias")
        button_view_queue.clicked.connect(self.mostrarTravessias) # Adiciona funcao para esse botao
        
        # Sai da aplicacao
        button_report = buttonMainMenu("Sair")
        button_report.clicked.connect(self.exitAplication) # Adiciona funcao para esse botao
  
        # Adiciona os botoes no layout
        layout.addWidget(button_add_element, alignment=CENTER)
        layout.addWidget(button_plot_drawn, alignment=CENTER)
        layout.addWidget(button_bst_info, alignment=CENTER)
        layout.addWidget(button_view_queue, alignment=CENTER)
        layout.addWidget(button_report, alignment=CENTER)
        
        widget.setLayout(layout) # Adiciona o layout no widget generico
  
        self.setCentralWidget(widget)  # Renderiza esse widget generico que foi criado 
  
    def plotarArvore(self):
        # 1. Verifica se a árvore está vazia
        if self.bst_manager.raiz is None:
            QMessageBox.warning(self, "Árvore Vazia", 
                                "Não há nada para plotar. Adicione elementos primeiro.")
            return

        # 2. Cria e exibe a nova janela de plotagem
        # Passamos a raiz da nossa árvore para a janela
        self.plot_window = PlotWindow(self.bst_manager.raiz)
        self.plot_window.show()
  
    def mostrarInformacoes(self):
        pass

    def mostrarTravessias(self):
        pass  

    def adicionarElemento(self):
        numero, ok = QInputDialog.getInt(self, 
                                          "Adicionar Elemento", 
                                          "Digite a chave (número natural):", 
                                          0, 0)
        
        if ok:
            self.bst_manager.inserir(numero)
            QMessageBox.information(self, "Sucesso", f"Elemento '{numero}' inserido na árvore.")

    # Sai da aplicacao
    def exitAplication(self):
        sys.exit()