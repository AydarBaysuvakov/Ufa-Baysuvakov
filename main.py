import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.e = []
        self.pushButton.clicked.connect(self.run)

    def run(self):
        r = randint(0, 300)
        self.e.append((randint(0, 400), randint(0, 600), r, r))
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_ufo(qp)
        qp.end()

    def draw_ufo(self, qp):
        qp.setBrush(QColor(250, 250, 0))
        for a in self.e:
            qp.drawEllipse(*a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())