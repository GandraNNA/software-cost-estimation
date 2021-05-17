import sys

from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QTableWidgetItem, QComboBox, QLabel
from PyQt5.uic import loadUi


class Complexity:
    EXTRA_LOW = 'Extra Low'
    VERY_LOW = 'Very Low'
    LOW = 'Low'
    NOMINAL = 'Nominal'
    HIGH = 'High'
    VERY_HIGH = 'Very High'
    EXTRA_HIGH = 'Extra High'


def getEmForPersValue(complexity):
    if complexity == Complexity.EXTRA_LOW:
        return 2.12
    if complexity == Complexity.VERY_LOW:
        return 1.62
    if complexity == Complexity.LOW:
        return 1.26
    if complexity == Complexity.NOMINAL:
        return 1
    if complexity == Complexity.HIGH:
        return 0.83
    if complexity == Complexity.VERY_HIGH:
        return 0.63
    if complexity == Complexity.EXTRA_HIGH:
        return 0.5
    return None

def getEmForRcpxValue(complexity):
    if complexity == Complexity.EXTRA_LOW:
        return  0.49
    if complexity == Complexity.VERY_LOW:
        return 0.6
    if complexity == Complexity.LOW:
        return 0.83
    if complexity == Complexity.NOMINAL:
        return  1
    if complexity == Complexity.HIGH:
        return 1.33
    if complexity == Complexity.VERY_HIGH:
        return 1.91
    if complexity == Complexity.EXTRA_HIGH:
        return 2.72
    return None

def getEmForRuseValue(complexity):
    if complexity == Complexity.LOW:
        return 0.95
    if complexity == Complexity.NOMINAL:
        return 1
    if complexity == Complexity.HIGH:
        return 1.07
    if complexity == Complexity.VERY_HIGH:
        return 1.15
    if complexity == Complexity.EXTRA_HIGH:
        return 1.24
    return None

def getEmForPdifValue(complexity):
    if complexity == Complexity.LOW:
        return 0.87
    if complexity == Complexity.NOMINAL:
        return  1
    if complexity == Complexity.HIGH:
        return 1.29
    if complexity == Complexity.VERY_HIGH:
        return 1.81
    if complexity == Complexity.EXTRA_HIGH:
        return 2.61
    return None

def getEmForPrexValue(complexity):
    if complexity == Complexity.EXTRA_LOW:
        return  1.59
    if complexity == Complexity.VERY_LOW:
        return 1.33
    if complexity == Complexity.LOW:
        return 1.22
    if complexity == Complexity.NOMINAL:
        return  1
    if complexity == Complexity.HIGH:
        return 0.87
    if complexity == Complexity.VERY_HIGH:
        return 0.74
    if complexity == Complexity.EXTRA_HIGH:
        return 0.62
    return None

def getEmForFcilValue(complexity):
    if complexity == Complexity.EXTRA_LOW:
        return  1.43
    if complexity == Complexity.VERY_LOW:
        return 1.3
    if complexity == Complexity.LOW:
        return 1.1
    if complexity == Complexity.NOMINAL:
        return  1
    if complexity == Complexity.HIGH:
        return 0.87
    if complexity == Complexity.VERY_HIGH:
        return 0.73
    if complexity == Complexity.EXTRA_HIGH:
        return 0.62
    return None

def getEmForScedValue(complexity):
    if complexity == Complexity.VERY_LOW:
        return 1.43
    if complexity == Complexity.LOW:
        return 1.14
    if complexity == Complexity.NOMINAL:
        return 1
    if complexity == Complexity.HIGH:
        return 1
    if complexity == Complexity.VERY_HIGH:
        return 1
    return None

def getEmForPrecValue(complexity):
    if complexity == Complexity.VERY_LOW:
        return 6.2
    if complexity == Complexity.LOW:
        return 4.96
    if complexity == Complexity.NOMINAL:
        return 3.72
    if complexity == Complexity.HIGH:
        return 2.48
    if complexity == Complexity.VERY_HIGH:
        return 1.24
    if complexity == Complexity.EXTRA_HIGH:
        return 0
    return None

def getEmForFlexValue(complexity):
    if complexity == Complexity.VERY_LOW:
        return 5.07
    if complexity == Complexity.LOW:
        return 4.05
    if complexity == Complexity.NOMINAL:
        return 3.04
    if complexity == Complexity.HIGH:
        return 2.03
    if complexity == Complexity.VERY_HIGH:
        return 1.01
    if complexity == Complexity.EXTRA_HIGH:
        return 0
    return None

def getEmForReslValue(complexity):
    if complexity == Complexity.VERY_LOW:
        return 7.07
    if complexity == Complexity.LOW:
        return 5.65
    if complexity == Complexity.NOMINAL:
        return 4.24
    if complexity == Complexity.HIGH:
        return 2.83
    if complexity == Complexity.VERY_HIGH:
        return 1.41
    if complexity == Complexity.EXTRA_HIGH:
        return 0
    return None

def getEmForTeamValue(complexity):
    if complexity == Complexity.VERY_LOW:
        return 5.48
    if complexity == Complexity.LOW:
        return 4.38
    if complexity == Complexity.NOMINAL:
        return 3.29
    if complexity == Complexity.HIGH:
        return 2.19
    if complexity == Complexity.VERY_HIGH:
        return 1.1
    if complexity == Complexity.EXTRA_HIGH:
        return 0
    return None

def getEmForPmatValue(complexity):
    if complexity == Complexity.VERY_LOW:
        return 7.8
    if complexity == Complexity.LOW:
        return 6.24
    if complexity == Complexity.NOMINAL:
        return 4.68
    if complexity == Complexity.HIGH:
        return 3.12
    if complexity == Complexity.VERY_HIGH:
        return 1.56
    if complexity == Complexity.EXTRA_HIGH:
        return 0
    return None

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        loadUi("COCOMO.ui", self)
        self.pushButton.clicked.connect(self.maths)

    def getText(self, object_name, object_class=QLineEdit):
        obj = self.findChild(object_class, object_name)
        if object_class == QLineEdit:
            return obj.text()
        if object_class == QComboBox:
            return obj.currentText()
        if object_class == QLabel:
            return obj.text()
        raise "getText(): Unexpected object class '" + object_class + "'."

    def getNumber(self, object_id, object_class=QLineEdit):
        try:
            return float(self.getText(object_id, object_class))
        except ValueError:
            return 0

    def maths(self):
        fieldPM = self.findChild(QLineEdit, 'PM')
        SIZE = self.getNumber('SIZE', QLineEdit)
        EAF = self.EMi()
        sumSF = self.SFj()
        A = 2.94
        B = 0.91
        E = B + (0.01 * sumSF)
        PM = EAF * A * (SIZE)**E
        fieldPM.setText(str(PM))

        fieldTM = self.findChild(QLineEdit, 'TM')
        C = 3.67
        D = 0.28
        SCED = getEmForScedValue(self.getText('EM_7', QComboBox))
        TM = SCED * C * (PM)**(D + (0.2 *(E - B)))
        fieldTM.setText(str(TM))


    def EMi(self):
        EAF = 1
        for i in range(0, 7):
            index_str = str(i + 1)
            nameEM = self.getText('nameEM_' + index_str, QLabel)
            if nameEM == 'PERS:':
                for k in range(0, 7):
                    index = str(k + 1)
                    complexity = self.getText('EM_' + index, QComboBox)
                    value = getEmForPersValue(complexity)
                    if value is not None:
                        EAF *= value
            elif nameEM == 'RCPX:':
                for k in range(0, 7):
                    index = str(k + 1)
                    complexity = self.getText('EM_' + index, QComboBox)
                    value = getEmForRcpxValue(complexity)
                    if value is not None:
                        EAF *= value
            elif nameEM == 'RUSE:':
                for k in range(0, 7):
                    index = str(k + 1)
                    complexity = self.getText('EM_' + index, QComboBox)
                    value = getEmForRuseValue(complexity)
                    if value is not None:
                        EAF *= value
            elif nameEM == 'PDIF:':
                for k in range(0, 7):
                    index = str(k + 1)
                    complexity = self.getText('EM_' + index, QComboBox)
                    value = getEmForPdifValue(complexity)
                    if value is not None:
                        EAF *= value
            elif nameEM == 'PREX:':
                for k in range(0, 7):
                    index = str(k + 1)
                    complexity = self.getText('EM_' + index, QComboBox)
                    value = getEmForPrexValue(complexity)
                    if value is not None:
                        EAF *= value
            elif nameEM == 'FCIL:':
                for k in range(0, 7):
                    index = str(k + 1)
                    complexity = self.getText('EM_' + index, QComboBox)
                    value = getEmForFcilValue(complexity)
                    if value is not None:
                        EAF *= value
            elif nameEM == 'SCED:':
                for k in range(0, 7):
                    index = str(k + 1)
                    complexity = self.getText('EM_' + index, QComboBox)
                    value = getEmForScedValue(complexity)
                    if value is not None:
                        EAF *= value
        return EAF

    def SFj(self):
        sumSF = 0.0
        for j in range(0, 5):
            index_str = str(j + 1)
            nameSF = self.getText('nameSF_' + index_str, QLabel)
            if nameSF == 'PREC:':
                for k in range(0, 5):
                    index = str(k + 1)
                    print('SF_' + index)
                    complexity = self.getText('EM_' + index, QComboBox)
                    value = getEmForPrecValue(complexity)
                    if value is not None:
                        sumSF += value
            elif nameSF == 'FLEX:':
                for k in range(0, 5):
                    index = str(k + 1)
                    complexity = self.getText('EM_' + index, QComboBox)
                    value = getEmForFlexValue(complexity)
                    if value is not None:
                        sumSF += value
            elif nameSF == 'RESL:':
                for k in range(0, 5):
                    index = str(k + 1)
                    complexity = self.getText('EM_' + index, QComboBox)
                    value = getEmForReslValue(complexity)
                    if value is not None:
                        sumSF += value
            elif nameSF == 'TEAM:':
                for k in range(0, 5):
                    index = str(k + 1)
                    complexity = self.getText('EM_' + index, QComboBox)
                    value = getEmForTeamValue(complexity)
                    if value is not None:
                        sumSF += value
            elif nameSF == 'PMAT:':
                for k in range(0, 5):
                    index = str(k + 1)
                    complexity = self.getText('EM_' + index, QComboBox)
                    value = getEmForPmatValue(complexity)
                    if value is not None:
                        sumSF += value
        return sumSF


if __name__ == "__main__":
    app = QApplication(sys.argv)
    appWindow = MyWindow()
    appWindow.show()
    sys.exit(app.exec())
