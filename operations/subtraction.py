import zope.interface
from interface_operation import IOperation

class Subtraction():
    zope.interface.implements(IOperation)

    def __init__(self):
        self.__name = 'Вычитание'
        self.__operands_count = 2
        self.__name_operands = {0: 'Уменьшаемое', 1: 'Вычитаемое'}

    def get_name_operation(self):
        return self.__name

    def get_name_operand(self, operand_number):
        return self.__name_operands[operand_number]

    def get_count_of_operands(self):
        return self.__operands_count

    def calculate(self, operands):
        return operands[0] - operands[1]