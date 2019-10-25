class OperationsManager():
    def __init__(self):
        self.__operations = []
        self.__operations_count = 0

    def get_operation(self, number):
        return self.__operations[number]

    def get_operations_count(self):
        return self.__operations_count

    def operations_load(self, path):
        #FIXME задание не понятно
        pass
