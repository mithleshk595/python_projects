stack = []

# push
stack.append("A")
stack.append("B")
stack.append("C")
print("stack: ", stack)

# peak
topElement = stack.pop()
print("peak: ", topElement)

# pop
poppedElement = stack.pop()
print("pop: ", poppedElement)

# stack after pop 
print("stack after pop: ", stack)

#isEmpty
isEmpty = not bool(stack)

# size
print("size: ", len(stack))