from zope.interface import implementer
from operations.interface_operation import IOperation
import operations.exceptions as exceptions
import math

@implementer(IOperation)
class Percent():

    def __init__(self):
        self.__name = 'Процент'
        self.__operands_count = 1
        self.__name_operands = {0: 'Число'}

    def get_name_operation(self):
        return self.__name

    def get_name_operand(self, operand_number):
        if (operand_number >= self.__operands_count):
            raise exceptions.OperationErrorException
        return self.__name_operands[operand_number]

    def get_count_of_operands(self):
        return self.__operands_count

    def calculate(self, operands):
        return operands[0] / 100


@implementer(IOperation)
class Power():

    def __init__(self):
        self.__name = 'Степень'
        self.__operands_count = 2
        self.__name_operands = {0: 'Число', 1: 'Степень'}

    def get_name_operation(self):
        return self.__name

    def get_name_operand(self, operand_number):
        if (operand_number >= self.__operands_count):
            raise exceptions.OperationErrorException
        return self.__name_operands[operand_number]

    def get_count_of_operands(self):
        return self.__operands_count

    def calculate(self, operands):
        return operands[0] ** operands[1]


@implementer(IOperation)
class SquareRoot():

    def __init__(self):
        self.__name = 'Квадратный корень'
        self.__operands_count = 1
        self.__name_operands = {0: 'Число'}

    def get_name_operation(self):
        return self.__name

    def get_name_operand(self, operand_number):
        if (operand_number >= self.__operands_count):
            raise exceptions.OperationErrorException
        return self.__name_operands[operand_number]

    def get_count_of_operands(self):
        return self.__operands_count

    def calculate(self, operands):
        return math.sqrt(operands[0])
