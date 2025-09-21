# x = [9, 12, 7, 4, 11]

# #Add element
# x.append

# #sort element
# x.sort

# print(x)


my_array = [7,12, 9, 4, 11, 8]
minval = my_array[0]

for i in my_array:
    if i < minval:
        minval = i

print("Lowest value:", minval)