class PriorityQueue:

    def __init__(self):
        self.queue = []

    # Function to heapify the tree
    def heapify(self, size, i):
        # Find the largest among root, left child and right child
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < size and self.queue[i] < self.queue[l]:
            largest = l

        if r < size and self.queue[largest] < self.queue[r]:
            largest = r

        # Swap and continue heapifying if root is not largest
        if largest != i:
            self.queue[i], self.queue[largest] = self.queue[largest], self.queue[i]
            self.heapify(size, largest)

    # Function to insert an element into the tree
    def insert(self, element):
        size = len(self.queue)
        if size == 0:
            self.queue.append(element)
        else:
            self.queue.append(element)
            for i in range((size // 2) - 1, -1, -1):
                self.heapify(size, i)

    # Function to delete an element from the tree
    def delete(self, element):
        size = len(self.queue)
        i = 0
        for i in range(0, size):
            if element == self.queue[i]:
                break

        self.queue[i], self.queue[size - 1] = self.queue[size - 1], self.queue[i]
        self.queue.remove(size - 1)

        for i in range((len(self.queue) // 2) - 1, -1, -1):
            self.heapify(len(self.queue), i)


q = PriorityQueue()

q.insert(3)
q.insert(4)
q.insert(9)
q.insert(5)
q.insert(2)
print(q.queue)
q.delete(4)
print(q.queue)