import math
import sys
from os import path

from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow
from PyQt5.uic import loadUi

number_of_estimates = 10


class PertWindow(QMainWindow):
    def __init__(self):
        super(PertWindow, self).__init__()
        ui_path = path.join(path.dirname(__file__), "PERT.ui")
        loadUi(ui_path, self)
        self.pushButton.clicked.connect(self.copyEstimatesNames)
        self.pushButton_Math.clicked.connect(self.maths)
        self.pushButton_Save.clicked.connect(self.saveTxt)

    def copyEstimatesNames(self):
        for i in range(1, number_of_estimates):
            index = str(i + 1)
            value = self.getText('estimate_' + index)
            for target_index in range(1, 5):
                target = self.findChild(QLineEdit, 'estimate' + str(target_index) + '_' + index)
                target.setText(value)
                target.adjustSize()

    def maths(self):
        value = self.getText('Name_project')
        target = self.findChild(QLineEdit, 'Name_project_1')
        target.setText(value)
        target.adjustSize()

        for i in range(0, number_of_estimates):
            index_str = str(i + 1)
            # ____Ei______________________________________________________________
            fieldEi = self.findChild(QLineEdit, 'E' + index_str)
            Ei = self.calcEi(self.getNumber('P' + index_str),
                             self.getNumber('M' + index_str),
                             self.getNumber('O' + index_str))
            fieldEi.setText(format(Ei, '.3f'))
            # ____CKOi____________________________________________________________
            fieldCKOi = self.findChild(QLineEdit, 'CKO' + index_str)
            CKOi = self.calcCKOi(self.getNumber('P' + index_str),
                                 self.getNumber('O' + index_str))
            fieldCKOi.setText(format(CKOi, '.3f'))
        # ___E________________________________________________________________
        fieldE = self.findChild(QLineEdit, 'E')
        E = 0
        for i in range(0, number_of_estimates):
            index_str = str(i + 1)
            E += self.calcE(self.getNumber('E' + index_str),
                            self.getNumber('K' + index_str))
        fieldE.setText(format(E, '.3f'))
        # ___CKO______________________________________________________________
        fieldCKO = self.findChild(QLineEdit, 'CKO')
        CKO = 0
        for i in range(0, number_of_estimates):
            index_str = str(i + 1)
            CKO += self.calcCKO(self.getNumber('K' + index_str),
                                self.getNumber('CKO' + index_str))
        fieldCKO.setText(format(CKO, '.3f'))
        # ___E95______________________________________________________________
        fieldE95 = self.findChild(QLineEdit, 'E95')
        E95 = self.calcE95(self.getNumber('E'),
                           self.getNumber('CKO'))
        fieldE95.setText(format(E95, '.3f'))
        # ___wmonth___________________________________________________________
        fieldwmonth = self.findChild(QLineEdit, 'wmonth')
        wmonth = 165 * 0.8
        fieldwmonth.setText(format(wmonth))
        # ___lintensity_______________________________________________________
        fieldlintensity = self.findChild(QLineEdit, 'lintensity')
        lintensity = self.cacllintensity(self.getNumber('E'),
                                         self.getNumber('wmonth'))
        fieldlintensity.setText(format(lintensity, '.3f'))
        # ___T________________________________________________________________
        fieldT = self.findChild(QLineEdit, 'T')
        T = self.calcT(self.getNumber('lintensity'))
        fieldT.setText(format(T, '.3f'))

    def getText(self, object_id):
        obj = self.findChild(QLineEdit, object_id)
        return obj.text()

    def getNumber(self, object_id):
        try:
            return float(self.getText(object_id))
        except ValueError:
            return 0

    def calcEi(self, p, m, o):
        return (p + 4 * m + o) / 6

    def calcCKOi(self, p, o):
        return (p - o) / 6

    def calcE(self, e, k):
        return e * k

    def calcCKO(self, k, cko):
        return math.sqrt(k * cko ** 2)

    def calcE95(self, e, cko):
        return e + 2 * cko

    def cacllintensity(self, e, wmonth):
        return e / wmonth

    def calcT(self, lintensity):
        return 2.5 * pow(lintensity, 1 / 3)

    def saveTxt(self):
        wmonth = self.getNumber('wmonth')
        name = self.getText('Name_project_1')
        lintensity = self.getNumber('lintensity')
        t = self.getNumber('T')
        with open(name + '_PERT.txt', 'w') as f:
            print('Метод PERT.', file=f)
            print('Сотрудник в месяц будет работать по проекту: ' + str(wmonth), file=f)
            print('Суммарная трудоёмкость проекта: ' + str(lintensity), file=f)
            print('Оптимальная продолжительность проекта: ' + str(t), file=f)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    appWindow = PertWindow()
    appWindow.show()
    sys.exit(app.exec())
