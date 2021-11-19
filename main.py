import sys
import random

from PyQt5 import uic
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def initUI(self):
        self.setGeometry(600, 600, 600, 600)
        self.setWindowTitle('Супрематизм')
        self.x = 0
        self.y = 0
        self.shape = -1
        self.setMouseTracking(True)

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        if self.shape == 0:
            self.qp.drawEllipse(self.x, self.y, random.randint(30, 255), random.randint(30, 255))
        elif self.shape == 1:
            self.qp.drawRect(self.x, self.y, random.randint(30, 255), random.randint(30, 255))
        elif self.shape == 2:
            self.qp.drawPolygon(QPolygon([QPoint(self.x, self.y),
                                          QPoint(self.x - random.randint(30, 255),
                                                 self.y + random.randint(30, 255)),
                                          QPoint(self.x + random.randint(30, 255),
                                                 self.y + random.randint(30, 255))]))
        self.qp.end()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.shape = 2
            self.repaint()

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()
        if event.button() == Qt.LeftButton:
            self.shape = 1
        elif event.button() == Qt.RightButton:
            self.shape = 0
        self.repaint()

    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())