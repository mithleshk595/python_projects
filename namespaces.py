# def fun1():
#     a = 45
#     print(a)
#     print(id(a))

#     def fun2():
#         b = 90
#         print(a)
#         print(id(a))
    
#     fun2()

# fun1()

a = 10
b = 20
c = 30

globals()["a"] = 25
globals()["b"] = 50
globals()["c"] = 75
print(a, b ,c)

