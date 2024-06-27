from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from qt_mimesis.ui.ui_main import Ui_MainWindow


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication([])
    application = Main()
    application.show()
    sys.exit(app.exec_())