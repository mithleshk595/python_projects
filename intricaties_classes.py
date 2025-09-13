class date:
    def __init__(self, d, m, y):
        self.__day, self.__mth, self.__yr = d, m, y

    def __eq__(self, other):
        if self.__day == other.__day and self.__mth == other.__mth and self.__yr == other.__yr:
            return True
        else:
            return False

d1 = date(17, 11, 98)
d2 = date(17, 11, 98)
d3 = date(19, 10, 98)
print(id(d1))
print(id(d2))
print(id(d3))
print(d1==d3)
