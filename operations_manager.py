import sys, inspect, glob, os
from zope.interface.verify import verifyObject
from zope.interface import providedBy
from operations.interface_operation import IOperation
import pyclbr
import importlib
import inspect

class OperationsManager():
    def __init__(self):
        self.__operations = []
        self.__operations_count = 0

    def get_operation(self, number):
        return self.__operations[number]

    def get_operations_count(self):
        return len(self.__operations)

    def operations_load(self, path):
        sep = '/'
        if sys.platform == 'win32' or sys.platform == 'cygwin':
            sep = '\\'
        for filename in glob.glob(os.path.join(path, '*.py')):
            try:
                module = importlib.import_module(filename.split(sep)[-2] +'.' + filename.split(sep)[-1].split('.')[0])
                for name, obj in inspect.getmembers(module):
                    try:
                        if inspect.isclass(obj) and IOperation.providedBy(obj()):
                            self.__operations.append(obj())
                    except:
                        continue
            except:
                continue
