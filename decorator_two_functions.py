def changecase(func):
    def myinner():
        return func().upper()
    return myinner
@changecase
def myfunctions():
    return "Hello sally"

@changecase
def otherfunction():
    return "I am speed!"

print(myfunctions())
print(otherfunction())
    