import zope.interface
from interface_operation import IOperation
import math

class SquareRoot():
    zope.interface.implements(IOperation)

    def __init__(self):
        self.__name = 'Квадратный корень'
        self.__operands_count = 1
        self.__name_operands = {0: 'Число'}

    def get_name_operation(self):
        return self.__name

    def get_name_operand(self, operand_number):
        return self.__name_operands[operand_number]

    def get_count_of_operands(self):
        return self.__operands_count

    def calculate(self, operands):
        return math.sqrt(operands[0])