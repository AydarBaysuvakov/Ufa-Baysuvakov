import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 400)
        self.e = []
        self.pushButton = QPushButton('Ellipce', self)
        self.pushButton.move(160, 190)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        r = randint(0, 300)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.e.append(((randint(0, 400), randint(0, 400), r, r), color))
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_ufo(qp)
        qp.end()

    def draw_ufo(self, qp):
        for a in self.e:
            qp.setBrush(a[1])
            qp.drawEllipse(*a[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())