import zope.interface
from interface_operation import IOperation

class Power():
    zope.interface.implements(IOperation)

    def __init__(self):
        self.__name = 'Степень'
        self.__operands_count = 2
        self.__name_operands = {0: 'Число', 1: 'Степень'}

    def get_name_operation(self):
        return self.__name

    def get_name_operand(self, operand_number):
        return self.__name_operands[operand_number]

    def get_count_of_operands(self):
        return self.__operands_count

    def calculate(self, operands):
        return operands[0] ** operands[1]