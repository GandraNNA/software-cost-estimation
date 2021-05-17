import sys
import math

from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow
from PyQt5.uic import loadUi


number_of_estimates = 10

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        loadUi("PERT.ui", self)
        # подключение клик-сигнал к слоту btnClicked
        self.pushButton.clicked.connect(self.copyEstimatesNames)
        self.pushButton_Math.clicked.connect(self.maths)

    def copyEstimatesNames(self):
        for i in range(0, number_of_estimates):
            index = str(i + 1)
            value = self.getText('estimate_' + index)
            for target_index in range(1, 5):
                target = self.findChild(QLineEdit, 'estimate' + str(target_index)  + '_'  + index)
                target.setText(value)
                target.adjustSize()

    def maths(self):
        for i in range(0, number_of_estimates):
            index_str = str(i + 1)
#____Ei______________________________________________________________
            fieldEi = self.findChild(QLineEdit, 'E' + index_str)
            Ei = self.calcEi(self.getNumber('P' + index_str),
                           self.getNumber('M' + index_str),
                           self.getNumber('O' + index_str))
            fieldEi.setText(str(Ei))
#____CKOi____________________________________________________________
            fieldCKOi = self.findChild(QLineEdit, 'CKO' + index_str)            
            CKOi = self.calcCKOi(self.getNumber('P' + index_str),
                                 self.getNumber('O' +index_str))
            fieldCKOi.setText(str(CKOi))
#___E________________________________________________________________
        fieldE = self.findChild(QLineEdit, 'E')
        E = 0
        for i in range(0, number_of_estimates):
            index_str = str(i + 1)
            E += self.calcE(self.getNumber('E' + index_str),
                            self.getNumber('K' + index_str))
        fieldE.setText(str(E)) 
#___CKO______________________________________________________________
        fieldCKO = self.findChild(QLineEdit, 'CKO')
        CKO = 0
        for i in range(0, number_of_estimates):
            index_str = str(i + 1)
            CKO += self.calcCKO(self.getNumber('K' + index_str),
                                self.getNumber('CKO' + index_str))
        fieldCKO.setText(str(CKO))
#___E95______________________________________________________________
        fieldE95 = self.findChild(QLineEdit, 'E95')
        E95 = self.calcE95(self.getNumber('E'),
                           self.getNumber('CKO'))
        fieldE95.setText(str(E95))
#___wmonth___________________________________________________________
        fieldwmonth = self.findChild(QLineEdit, 'wmonth')
        wmonth = 165 * 0.8
        fieldwmonth.setText(str(wmonth))
#___lintensity_______________________________________________________
        fieldlintensity = self.findChild(QLineEdit, 'lintensity')
        lintensity = self.cacllintensity(self.getNumber('E'),
                                         self.getNumber('wmonth'))
        fieldlintensity.setText(str(lintensity))
#___T________________________________________________________________
        fieldT = self.findChild(QLineEdit, 'T')
        T = self.calcT(self.getNumber('lintensity'))
        fieldT.setText(str(T))


    def getText(self, object_id):
        obj = self.findChild(QLineEdit, object_id)
        return obj.text()

    def getNumber(self, object_id):
        try:
            return float(self.getText(object_id))
        except ValueError:
            return 0

    def calcEi(self, p, m, o):
        return (p + 4*m + o) / 6

    def calcCKOi(self, p, o):
        return (p - o) / 6

    def calcE(self, e, k):
        return e * k

    def calcCKO(self, k, cko):
        return math.sqrt(k * cko**2)

    def calcE95(self, e, cko):
        return e + 2 * cko

    def cacllintensity(self, e, wmonth):
        return e / wmonth

    def calcT(self, lintensity):
        return 2.5 * pow(lintensity, 1/3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    appWindow = MyWindow()
    appWindow.show()
    sys.exit(app.exec())
