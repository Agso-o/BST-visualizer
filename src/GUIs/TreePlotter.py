import sys
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QSizePolicy
)
from PySide6.QtGui import QPainter, QPen, QBrush, QFont, QColor
from PySide6.QtCore import Qt, QPointF, QRectF

class TreeWidget(QWidget):
    """Widget que desenha a árvore."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.bst_root = None
        self.node_radius = 20
        self.v_spacing = 60
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setMinimumSize(400, 300)

    def set_tree_root(self, root):
        self.bst_root = root
        self.update()  

    def paintEvent(self, event):
        super().paintEvent(event)
        if not self.bst_root:
            return
            
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        font = QFont("Arial", 10, QFont.Weight.Bold)
        painter.setFont(font)
        
        start_x = self.width() / 2
        start_y = self.node_radius + 20
        initial_h_spacing = self.width() / 4

        self._draw_node_recursive(painter, self.bst_root, start_x, start_y, initial_h_spacing)

    def _draw_node_recursive(self, painter, node, x, y, h_spacing):
        if node is None:
            return
        
        if node.esq:
            left_x = x - h_spacing
            left_y = y + self.v_spacing
            pen_line = QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine)
            painter.setPen(pen_line)
            painter.drawLine(QPointF(x, y), QPointF(left_x, left_y))
            self._draw_node_recursive(painter, node.esq, left_x, left_y, h_spacing / 2)

        if node.dir:
            right_x = x + h_spacing
            right_y = y + self.v_spacing
            pen_line = QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine)
            painter.setPen(pen_line)
            painter.drawLine(QPointF(x, y), QPointF(right_x, right_y))
            self._draw_node_recursive(painter, node.dir, right_x, right_y, h_spacing / 2)

        pen_node = QPen(Qt.GlobalColor.black, 2)
        brush_node = QBrush(QColor("#FFFFFF")) # Fundo branco
        painter.setPen(pen_node)
        painter.setBrush(brush_node)
        
        diameter = self.node_radius * 2
        node_rect = QRectF(x - self.node_radius, y - self.node_radius, diameter, diameter)
        
        painter.drawEllipse(node_rect)
        
        pen_text = QPen(Qt.GlobalColor.black)
        painter.setPen(pen_text)
        painter.drawText(node_rect, Qt.AlignmentFlag.AlignCenter, str(node.key))


class PlotWindow(QWidget):
    """Esta é a nova janela que abre para mostrar a árvore."""
    def __init__(self, bst_root, parent=None):
        super().__init__(parent)
        
        # Define atributos da janela
        self.setWindowTitle("Visualizador de Árvore (Plotado)")
        self.setGeometry(200, 200, 800, 600) # Posição (x,y) e Tamanho (w,h)

        # 1. Configura o layout e o widget de desenho
        main_layout = QVBoxLayout(self)
        self.tree_widget = TreeWidget()
        
        # Adiciona um botão para fechar
        self.btn_close = QPushButton("Fechar")
        self.btn_close.clicked.connect(self.close) # self.close() é um método nativo do QWidget
        
        main_layout.addWidget(self.tree_widget)
        main_layout.addWidget(self.btn_close)
        self.setLayout(main_layout)

        # 2. Passa a raiz da árvore para o widget de desenho
        self.tree_widget.set_tree_root(bst_root)