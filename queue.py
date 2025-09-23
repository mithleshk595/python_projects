queue = []

#Enqueue

queue.append("A")
queue.append("B")
queue.append("C")
print("Queue:" , queue)

#dequeue
poppedElement = queue.pop(0)
print("Dequeue: ", poppedElement)

print("Queue after Dequeue: ", queue)

# isEmpty
# Peek
frontElement = queue[0]
print("Peek: ", frontElement)


isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

# Size
print("Size: ", len(queue))




