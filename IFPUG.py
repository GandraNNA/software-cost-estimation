import sys

from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QTableWidgetItem, QComboBox
from PyQt5.uic import loadUi

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        loadUi("IFPUG.ui", self)
        self.pushButton.clicked.connect(self.maths)

    def getText(self, object_name, object_class=QLineEdit):
        #print(object_name)
        obj = self.findChild(object_class, object_name)
        if object_class == QLineEdit:
            return obj.text()
        if object_class == QComboBox:
            return obj.currentText()
        raise "getText(): Unexpected object class '" + object_class + "'."

    def getNumber(self, object_id, object_class=QLineEdit):
        try:
            return float(self.getText(object_id, object_class))
        except ValueError:
            return 0


    def maths(self):
#____TDI______________________________________________________________        
        fieldTDI = self.findChild(QLineEdit, 'TDI')
        TDI = 0        
        for i in range(0, 14):
            index_str = str(i + 1)
            TDI += self.getNumber('DI_' + index_str, QComboBox)
        fieldTDI.setText(str(TDI))


        for i in range(0, 20):
            complexity = '---'
            index_str = str(i + 1)
            fieldcomplexity = self.findChild(QLineEdit, 'complexity_' + index_str)
            det = self.getNumber('DET_' + index_str)
            ret_ftr = self.getNumber('RetFtr_' + index_str)

            if self.getText('type_' + index_str, QComboBox) in ['ILF', 'EIF']:
                if (1 <= det and det <= 19) and (ret_ftr == 1):
                    complexity = 'low'
                elif (20 <= det and det < 50) and (ret_ftr == 1):
                    complexity = 'low'
                elif (det >= 50) and (ret_ftr == 1):
                    complexity = 'average'

                if (1 <= det and det <= 19) and (2 <= ret_ftr and ret_ftr <= 5):
                    complexity = 'low'
                elif (20 <= det and det < 50) and (2 <= ret_ftr and ret_ftr <= 5):
                    complexity = 'average'
                elif (det >= 50) and (2 <= ret_ftr and ret_ftr <= 5):
                    complexity = 'high'

                if (1 <= det and det <= 19) and (ret_ftr >= 6):
                    complexity = 'average'
                if (20 <= det and det < 50) and (ret_ftr >= 6):
                    complexity = 'high'
                elif (det >= 50) and (ret_ftr >= 6):
                    complexity = 'high'
#______________________________________________________________________
            if self.getText('type_' + index_str, QComboBox) in ['EI']:
                if (1 <= det and det <= 4) and (0 < ret_ftr and ret_ftr < 2):
                    complexity = 'low'
                elif (5 <= det and det <= 15) and (0 < ret_ftr and ret_ftr < 2):
                    complexity = 'low'
                elif (det >= 16) and (0 < ret_ftr and ret_ftr < 2):
                    complexity = 'average'

                if (1 <= det and det <= 4) and (ret_ftr == 2):
                    complexity = 'low'
                elif (5 <= det and det <= 15) and (ret_ftr == 2):
                    complexity = 'average'
                elif (det >= 16) and (ret_ftr == 2):
                    complexity = 'high'

                if (1 <= det and det <= 4) and (ret_ftr >= 3):
                    complexity = 'average'
                elif (5 <= det and det <= 15) and (ret_ftr >= 3):
                    complexity = 'high'
                elif (det >= 16) and (ret_ftr >= 3):
                    complexity = 'high'
#__________________________________________________________________________
            if self.getText('type_' + index_str, QComboBox) in ['EO', 'EQ']:

                if (1 <= det and det <= 5) and (0 < ret_ftr and ret_ftr < 2):
                    complexity = 'low'
                elif (6 <= det and det <= 19) and (0 < ret_ftr and ret_ftr < 2):
                    complexity = 'low'
                elif (det >=20) and (0 < ret_ftr and ret_ftr < 2):
                    complexity = 'average'

                if (1 <= det and det <= 5) and (2 <= ret_ftr and ret_ftr <= 3):
                    complexity = 'low'
                elif (6 <= det and det <= 19) and (2 <= ret_ftr and ret_ftr <= 3):
                    complexity = 'average'
                elif (det >=20) and (2 <= ret_ftr and ret_ftr <= 3):
                    complexity = 'high'

                if (1 <= det and det <= 5) and (ret_ftr >= 4):
                    complexity = 'average'
                elif (6 <= det and det <= 19) and (ret_ftr >= 4):
                    complexity = 'high'
                elif (20 <= det) and (ret_ftr >= 4):
                    complexity = 'high'
            fieldcomplexity.setText(str(complexity))

        for i in range(0, 20):
            FP = '---'
            index_str = str(i + 1)
            fieldFP = self.findChild(QLineEdit, 'FP_' + index_str)
            if self.getText('type_' + index_str, QComboBox) in ['ILF']:
                if self.getText('complexity_' + index_str) == 'low':
                    FP = 7
                elif self.getText('complexity_' + index_str) == 'average':
                    FP = 10
                elif self.getText('complexity_' + index_str) == 'high':
                    FP = 15
            if self.getText('type_' + index_str, QComboBox) in ['EIF']:
                if self.getText('complexity_' + index_str) == 'low':
                    FP = 5
                elif self.getText('complexity_' + index_str) == 'average':
                    FP = 7
                elif self.getText('complexity_' + index_str) == 'high':
                    FP = 10
            if self.getText('type_' + index_str, QComboBox) in ['EI']:
                if self.getText('complexity_' + index_str) == 'low':
                    FP = 3
                elif self.getText('complexity_' + index_str) == 'average':
                    FP = 4
                elif self.getText('complexity_' + index_str) == 'high':
                    FP = 6
            if self.getText('type_' + index_str, QComboBox) in ['EO']:
                if self.getText('complexity_' + index_str) == 'low':
                    FP = 4
                elif self.getText('complexity_' + index_str) == 'average':
                    FP = 5
                elif self.getText('complexity_' + index_str) == 'high':
                    FP = 7
            if self.getText('type_' + index_str, QComboBox) in ['EQ']:
                if self.getText('complexity_' + index_str) == 'low':
                    FP = 3
                elif self.getText('complexity_' + index_str) == 'average':
                    FP = 4
                elif self.getText('complexity_' + index_str) == 'high':
                    FP = 6
            fieldFP.setText(str(FP))

#____UFP______________________________________________________________        
        fieldUFP = self.findChild(QLineEdit, 'UFP')
        UFP = 0
        for i in range(0, 20):
            index_str = str(i + 1)
            UFP += self.getNumber('FP_' + index_str, QLineEdit)
        fieldUFP.setText(str(UFP))

        fieldAFP = self.findChild(QLineEdit, 'AFP')
        AFP = 0        
        AFP = self.calcAPF(self.getNumber('UFP'),
                           self.getNumber('TDI'))
        fieldAFP.setText(str(AFP))


    def calcAPF(self, ufp, tdi):
        return ufp * ((tdi * 0.1) + 0.65)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    appWindow = MyWindow()
    appWindow.show()
    sys.exit(app.exec())
