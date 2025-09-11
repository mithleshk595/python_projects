# def fibo(old, current, terms):
#     if terms >= 1:
#         new = old + current
#         print(f"{new}", end= ".\t")
#         terms = terms -1
#         fibo(current, new, terms)

# old = 1
# Current = 1
# print(f"{old}", end= "\t")
# print(f"{Current}", end="\t")
# fibo(old, Current, 13)


import sys

def dec_to_binary(n):
    r = n % 2
    n = int(n / 2)
    if n !=0:
        dec_to_binary(n)
    print(r, end= "")


sys.setrecursionlimit(10 ** 6)
num = int(input("Enter the number :"))
print("The binary equivalent is :")
dec_to_binary(num)

