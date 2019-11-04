import sys
from design import Ui_Form
from operations_manager import OperationsManager
import operations.exceptions as exceptions
from PyQt5 import QtWidgets


class Controller(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.operations_manager = OperationsManager()
        self.operations_manager.operations_load('/home/ksenia/Desktop/Calc/operations')
        self.make_list_operations()
        self.selected_operation()
        self.comboBox.currentIndexChanged.connect(self.selected_operation)
        self.lineEdit.textChanged.connect(self.check_operand)
        self.lineEdit_2.textChanged.connect(self.check_operand)
        self.pushButton_3.clicked.connect(self.calculate)
        self.pushButton.clicked.connect(lambda: self.copy(1))
        self.pushButton_2.clicked.connect(lambda: self.copy(2))
        self.lineEdit_3.setReadOnly(True)

    def make_list_operations(self):
        count = self.operations_manager.get_operations_count()
        i = 0
        while i < count:
            self.comboBox.addItem(self.operations_manager.get_operation(i).get_name_operation())
            i = i + 1

    def check_operand(self):
        try:
            if self.lineEdit.text() != "":
                float(self.lineEdit.text())
            self.lineEdit.setStyleSheet("QLineEdit {background-color:white}")
        except:
            self.lineEdit.setStyleSheet("QLineEdit {background-color:red}")
            self.lineEdit.setText("число")
        if self.operation.get_count_of_operands() == 2:
            try:
                if self.lineEdit_2.text() != "":
                    float(self.lineEdit_2.text())
                self.lineEdit_2.setStyleSheet("QLineEdit {background-color:white}")
            except:
                self.lineEdit_2.setStyleSheet("QLineEdit {background-color:red}")
                self.lineEdit_2.setText("число")

    def selected_operation(self):
        self.operation = self.operations_manager.get_operation(self.comboBox.currentIndex())
        if self.operation.get_count_of_operands() == 1:
            try:
                self.lineEdit.setPlaceholderText(self.operation.get_name_operand(0))
            except exceptions.OperationErrorException:
                self.lineEdit.setPlaceholderText("")
            self.lineEdit_2.hide()
            self.pushButton_2.hide()
        elif self.operation.get_count_of_operands() == 2:
            try:
                self.lineEdit.setPlaceholderText(self.operation.get_name_operand(0))
            except exceptions.OperationErrorException:
                self.lineEdit.setPlaceholderText("")
            try:
                self.lineEdit_2.setPlaceholderText(self.operation.get_name_operand(1))
            except exceptions.OperationErrorException:
                self.lineEdit_2.setPlaceholderText("")
            self.lineEdit_2.show()
            self.pushButton_2.show()

    def calculate(self):
        if self.operation.get_count_of_operands() == 1:
            self.lineEdit_3.setText(str(self.operation.calculate([float(self.lineEdit.text())])))
        elif self.operation.get_count_of_operands() == 2:
            self.lineEdit_3.setText(str(self.operation.calculate([float(self.lineEdit.text())] + [float(self.lineEdit_2.text())])))

    def copy(self, index):
        if index == 1:
            self.lineEdit.setText(self.lineEdit_3.text())
        else:
            self.lineEdit_2.setText(self.lineEdit_3.text())
        self.lineEdit_3.setText("")

    
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Controller()  # Создаём объект класса Controller
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__': 
    main()  
