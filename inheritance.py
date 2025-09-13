from abc import ABC, abstractclassmethod
class printer(ABC):
    def __init__(self, n):
        self.__name = n
    
    @abstractclassmethod
    def print(self, docName):
        pass

class laserprinter(printer):
    def __init__(self, n):
        super().__init__(n)
    
    def print(self, docName):
        print(">> Laserprinter.print")
        print("Trying to print :", docName)
    
class inkjetprinter(printer):
    def __init__(self, n):
        super().__init__(n)
    
    def print(self, docName):
        print(">> inketprinter.print")
        print("Trying to print :", docName)


p = laserprinter("Laserjet 1100")
p.print("hello1.pdf")
p = inkjetprinter("IBM 2140")
p.print("hello2.doc")

