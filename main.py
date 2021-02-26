import random
import sys
import sys

from PyQt5 import QtCore, QtGui
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.add)
        self.flag = False
        self.type = None

    def draw(self):
        for i in range(random.randrange(1, 9)):
            ln = random.randint(1, 300)
            x, y = random.randrange(210, 590), random.randrange(210, 490)
            self.qp.setBrush(QColor(255, 255, 0))
            self.qp.drawEllipse(x - ln // 2, y - ln // 2, ln, ln)

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def add(self):
        self.flag = True
        self.update()


def except_hook(cls, exception, traceback):
    print(cls, exception, traceback)
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
