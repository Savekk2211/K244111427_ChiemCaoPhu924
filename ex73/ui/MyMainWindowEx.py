from chap5.ex73.libra.mymodule import solve_quadratic
from chap5.ex73.ui.MyMainWindow import Ui_MainWindow

class MyMainWindowEx(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def show_window(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButton.clicked.connect(self.solve)
    def solve(self):
        a = int(self.aLineEdit.text())
        b = int(self.bLineEdit.text())
        c = int(self.cLineEdit.text())
        result =solve_quadratic(a, b, c)
        self.resultLineEdit.setText(str(result))