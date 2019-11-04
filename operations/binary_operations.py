from zope.interface import implementer
from operations.interface_operation import IOperation
import operations.exceptions as exceptions

@implementer(IOperation)
class Addition():

    def __init__(self):
        self.__name = 'Сложение'
        self.__operands_count = 2
        self.__name_operands = {0: 'Первое слагаемое', 1: 'Второе слагаемое'}

    def get_name_operation(self):
        return self.__name

    def get_name_operand(self, operand_number):
        if (operand_number >= self.__operands_count):
            raise exceptions.OperationErrorException
        return self.__name_operands[operand_number]

    def get_count_of_operands(self):
        return self.__operands_count

    def calculate(self, operands):
        try:
            return float(operands[0]) + float(operands[1])
        except ValueError:
            raise exceptions.InvalidOperandException


@implementer(IOperation)
class Division():

    def __init__(self):
        self.__name = 'Деление'
        self.__operands_count = 2
        self.__name_operands = {0: 'Делимое', 1: 'Делитель'}

    def get_name_operation(self):
        return self.__name

    def get_name_operand(self, operand_number):
        if operand_number >= self.__operands_count:
            raise exceptions.OperationErrorException
        return self.__name_operands[operand_number]

    def get_count_of_operands(self):
        return self.__operands_count

    def calculate(self, operands):
        try:
            return float(operands[0]) / float(operands[1])
        except ValueError:
            raise exceptions.InvalidOperandException
        except ZeroDivisionError:
            raise exceptions.OperationErrorException



@implementer(IOperation)
class Multiplication():

    def __init__(self):
        self.__name = 'Умножение'
        self.__operands_count = 2
        self.__name_operands = {0: 'Первый множитель', 1: 'Второй множитель'}

    def get_name_operation(self):
        return self.__name

    def get_name_operand(self, operand_number):
        if (operand_number >= self.__operands_count):
            raise exceptions.OperationErrorException
        return self.__name_operands[operand_number]

    def get_count_of_operands(self):
        return self.__operands_count

    def calculate(self, operands):
        try:
            return float(operands[0]) * float(operands[1])
        except ValueError:
            raise exceptions.InvalidOperandException


@implementer(IOperation)
class Subtraction():

    def __init__(self):
        self.__name = 'Вычитание'
        self.__operands_count = 2
        self.__name_operands = {0: 'Уменьшаемое', 1: 'Вычитаемое'}

    def get_name_operation(self):
        return self.__name

    def get_name_operand(self, operand_number):
        if (operand_number >= self.__operands_count):
            raise exceptions.OperationErrorException
        return self.__name_operands[operand_number]

    def get_count_of_operands(self):
        return self.__operands_count

    def calculate(self, operands):
        try:
            return float(operands[0]) - float(operands[1])
        except ValueError:
            raise exceptions.InvalidOperandException


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
        try:
            return float(operands[0]) ** float(operands[1])
        except ValueError:
            raise exceptions.InvalidOperandException