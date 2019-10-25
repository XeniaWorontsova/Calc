import zope.interface

class IOperation(zope.interface.Interface):
    def get_name_operation():
        """
            Возвращает имя операции.

            Возвращаемое значение: str
        """

    def get_name_operand(operand_number):
        """
            Возвращает имя операнда.

            Входные параметры:
                operand_number(int): номер операнда.

            Возвращаемое значение: str
        """

    def get_count_of_operands():
        """
            Возвращает количество операндов.

            Возвращаемое значение: int.
        """

    def calculate(operands):   
        """
            Производит рассчет.

            Входные параметры:
                operands(list): операнды.

            Возвращаемое значение: float.
        """

    