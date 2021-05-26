from enum import Enum
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

from COCOMO import CocomoWindow
from IFPUG import IfpugWindow
from PERT import PertWindow


class ChildWindowType(Enum):
    COCOMO = "COCOMO"
    IFPUG = "IFPUG"
    PERT = "PERT"


# To keep a reference to a child window.
child_window = None


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main.ui", self)
        self.COCOMO_button.clicked.connect(self.openCocomoWindow)
        self.IFPUG_button.clicked.connect(self.openIfpugWindow)
        self.PERT_button.clicked.connect(self.openPertWindow)

    def openCocomoWindow(self):
        self.openChildWindow(ChildWindowType.COCOMO)

    def openIfpugWindow(self):
        self.openChildWindow(ChildWindowType.IFPUG)

    def openPertWindow(self):
        self.openChildWindow(ChildWindowType.PERT)

    def openChildWindow(self, child_window_type):
        global child_window
        if child_window_type == ChildWindowType.COCOMO:
            child_window = CocomoWindow()
        elif child_window_type == ChildWindowType.IFPUG:
            child_window = IfpugWindow()
        elif child_window_type == ChildWindowType.PERT:
            child_window = PertWindow()

        assert child_window is not None
        child_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    appWindow = MainWindow()
    appWindow.show()
    sys.exit(app.exec())
