def factorize(n, i):
    if i <= n:
        if n % i == 0:
            print(i, end=",")
            n = n//i
        else:
            i += 1
    factorize(n, i)

num = int(input("Enter a number:"))
print("prime factors are: ")
factorize(num ,2)

def rsum(num):
    if num !=0:
        digit = num % 10
        num = int(num/10)
        sum = digit + rsum(num)
    else:
        return 0
    return sum

n = int(input("Enter number: "))
rs = rsum(n)
print("Sum of digits =", rs)


def papersizes(i, n, l, b):
    if n !=0:
        print(f"A(i): L = {int(l)} B ={int(b)}")
        newb = l / 2
        newl = b
        n -= 1
        i += 1
        papersizes(i, n, newl, newb)

papersizes(0, 7, 1189, 841)





