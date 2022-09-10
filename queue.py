class Queue:

    def __init__(self):
        self.queue = []

    # Enqueue
    def enqueue(self, element):
        self.queue.append(element)

    # Dequeue
    def dequeue(self):
        if len(self.queue) < 1:
            return "Queue is Empty"
        return self.queue.pop(0)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.queue)
q.dequeue()
print(q.queue)