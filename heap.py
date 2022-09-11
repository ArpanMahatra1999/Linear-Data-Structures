class Heap:

    def __init__(self):
        self.values = []

    # Max Heap
    def heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.values[largest] < self.values[l]:
            largest = l

        if r < n and self.values[largest] < self.values[r]:
            largest = r

        if largest != i:
            self.values[i], self.values[largest] = self.values[largest], self.values[i]
            self.heapify(n, largest)

    # Insertion
    def insert(self, new):
        size = len(self.values)
        if size == 0:
            self.values.append(new)
        else:
            self.values.append(new)
            for i in range((size // 2) - 1, -1, -1):
                self.heapify(size, i)

    # Deletion
    def delete(self, num):
        size = len(self.values)
        for i in range(0, size):
            if num == self.values[i]:
                self.values[i], self.values[size - 1] = self.values[size - 1], self.values[i]
                self.values.remove(num)
                for j in range((len(self.values) // 2) - 1, -1, -1):
                    self.heapify(len(self.values), j)
                break


h = Heap()
h.insert(3)
h.insert(4)
h.insert(9)
h.insert(5)
h.insert(2)
print("Max-Heap array: " + str(h.values))
h.delete(5)
print("After deleting an element: " + str(h.values))
