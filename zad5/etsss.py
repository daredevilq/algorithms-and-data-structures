from queue import PriorityQueue
from queue import Queue
queue=PriorityQueue()

queue.put((10,1))
queue.put((5,5))
queue.put((20,1))

print(queue.get())
print(queue.get())
print(queue.get())

queue=Queue()

queue.put((10,1))
queue.put((5,5))
queue.put((20,1))

print(queue.get())
print(queue.get())
print(queue.get())


test=PriorityQueue()
test.put((0,1))
print(test.get())