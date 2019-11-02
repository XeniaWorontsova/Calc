import sys
from design import Ui_Form
from operations_manager import OperationsManager
from PyQt5 import QtWidgets


class Controller(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.operations_manager = OperationsManager()
        self.operations_manager.operations_load('/home/ksenia/Desktop/Calc/operations')
        self.make_list_operations()

    def make_list_operations(self):
        count = self.operations_manager.get_operations_count()
        i = 0
        while i < count:
            self.comboBox.addItem(self.operations_manager.get_operation(i).get_name_operation())
            i = i + 1

    def check_operand(self):
        pass
    
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Controller()  # Создаём объект класса Controller
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__': 
    main()  
