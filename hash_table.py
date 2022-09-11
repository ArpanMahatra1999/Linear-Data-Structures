class HashTable:

    def __init__(self):
        self.table = [None, ]*10

    # Hash Function
    def hashFunction(self, key):
        return key % 10

    # Insertion
    def insertData(self, key, value):
        index = self.hashFunction(key)
        self.table[index] = [key, value]

    # Deletion
    def deleteData(self, key):
        index = self.hashFunction(key)
        self.table[index] = None


ht = HashTable()
ht.insertData(123, "apple")
ht.insertData(432, "mango")
ht.insertData(213, "banana")
ht.insertData(654, "guava")
print(ht.table)
ht.deleteData(213)
print(ht.table)
