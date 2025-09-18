def changescase(func):
    def myinner():
        return func().upper()
    return myinner
@changescase
def myfunction():
    return "Hello sally"
print(myfunction())