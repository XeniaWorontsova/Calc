import sys
from design import Ui_Form
from operations_manager import OperationsManager
from PyQt5 import QtWidgets


class Controller(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.operations_manager = OperationsManager()

    def make_list_operations(self):
        count = self.operations_manager.get_operations_count
        i = 0
        while i < count:
            self.comboBox.addItem(self.operations_manager.get_operation(i))

    def check_operand(self):
        #FIXME при change edit_line, но по заданию не так. 
        #Уточнить, зачем в контроллер передавать edit_line - это просто привязка к си шарпу? 
        #ПОПРОСИТЬ ОБЪЯСНИТЬ ВСЮ СТРУКТУРУ КОНТРОЛЛЕРА ЗАНОВО
        pass
    
    
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Controller()  # Создаём объект класса Controller
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__': 
    main()  
