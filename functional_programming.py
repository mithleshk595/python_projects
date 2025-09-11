# def fun():
#     print("ln fun")

# def disp():
#     print("ln disp")

# def msg():
#     print("ln msg")

# lst = [fun, disp, msg]
# for f in lst:
#     f()


lst1 = [1, 2 ,3, 4, 5, 6]
lst2 = [6, 5, 4, 3, 2, 1]

result = map(lambda n1, n2:n1 + n2, lst1, lst2)
print(list(result))


