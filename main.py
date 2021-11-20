import sys
import random

from PyQt5 import uic
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPolygon, QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        self.ok = False

    def run(self):
        self.ok = True
        self.update()

    def paintEvent(self, event):
        if self.ok:
            self.qp = QPainter()
            # Начинаем процесс рисования
            self.qp.begin(self)
            self.draw_flag()
            self.qp.end()

    def draw_flag(self):
        # Задаем кисть
        size = random.randint(0, 250)
        self.qp.setBrush(QColor('yellow'))
        self.qp.drawEllipse(130, 200, size, size)
        # Рисуем прямоугольник заданной кистью


def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())