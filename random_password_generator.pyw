import random
from string import digits, punctuation, ascii_letters
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
import pyperclip


class RandomPassword(QtWidgets.QMainWindow):
    def __init__(self):
        super(RandomPassword, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Random Password Generator')
        self.setWindowIcon(QIcon('ico.png'))
        self.ui.length.setText('0')
        self.ui.generate_pass.clicked.connect(self.generate_pass)
        self.ui.copy.clicked.connect(self.copy_pass)
        self.ui.clear.clicked.connect(self.clear_all)

    def generate_pass(self):
        chars = digits + punctuation + ascii_letters
        password = ''
        length = int(self.ui.length.text())
        if length == 0:
            password = 'Length can not be zero!'
        else:
            for i in range(length):
                if length > 30:
                    password = 'Password is very long'
                else:
                    password += random.choice(chars)

        self.ui.password.setText(password)

    def copy_pass(self):

        if self.ui.password.text():
            pyperclip.copy(self.ui.password.text())
            self.ui.password.setText('Password was copied!')
        else:
            self.ui.password.setText('Password field is empty!')

    def clear_all(self):

        self.ui.length.setText('')
        self.ui.password.setText('')


app = QtWidgets.QApplication([])
application = RandomPassword()
application.show()

sys.exit(app.exec_())
