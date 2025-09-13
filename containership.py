class Base:
    def __method(self):
        print("in base.__method")
    
    def function(self):
        self.__method()
    
class derived(Base):
    def __method(self):
        print("in  drived.__method")

b = Base()
b.function()
d = derived()
d.function()
