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
        if len(operands) > self.__operands_count:
            raise exceptions.InvalidOperandException
        return float(operands[0]) / 100


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
        if len(operands) > self.__operands_count:
            raise exceptions.InvalidOperandException
        try:
            return math.sqrt(float(operands[0]))
        except:
            raise exceptions.OperationErrorException
