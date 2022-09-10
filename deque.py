class Deque:
    def __init__(self):
        self.queue = []

    # Inserts
    def addRear(self, item):
        self.queue.append(item)

    def addFront(self, item):
        self.queue.insert(0, item)

    # Delete
    def removeFront(self):
        return self.queue.pop(0)

    def removeRear(self):
        return self.queue.pop()


d = Deque()
d.addRear(8)
d.addRear(5)
d.addFront(7)
d.addFront(10)
d.addRear(11)
print(d.removeRear())
print(d.removeFront())
d.addFront(55)
d.addRear(45)
print(d.queue)
