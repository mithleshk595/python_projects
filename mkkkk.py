number = int(input("pleas enter the range: "))

first  = 0
second = 1

for num in range (0, number):
    if(num <= 1):
        next = num
    else:
        next = first + second
        first = second
        second = next
    print(next)
    
