def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        return -1
mylist = [10, 20, 30, 40, 500]
x = 500
result = linearSearch(mylist, x)
if result != -1:
    print("Elemrnt found at index", result)
else:
    print("Element not found in the index")
    

