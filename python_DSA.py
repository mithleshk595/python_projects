class stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return self.stack.pop()
        
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

# create a stack 
mystack = stack()

mystack.push("A")
mystack.push("B")
mystack.push("C")

print("stack: ", mystack.stack)
print("pop: ", mystack.pop)
print("stack after pop: ", mystack.stack)
print("peek: ", mystack.peek)
print("isEmpty: ", mystack.isEmpty)
print("size: ", mystack.size)
