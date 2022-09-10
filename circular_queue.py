class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    # Enqueue
    def enqueue(self, element):
        if (self.rear + 1) % self.size == self.front:
            print("The circular queue is full\n")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = element
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element

    # Dequeue
    def dequeue(self):
        if self.front == -1:
            print("The circular queue is empty\n")
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp


q = CircularQueue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
print(q.queue)
