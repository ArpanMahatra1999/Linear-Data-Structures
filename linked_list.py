# Create a Node
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Create a Linked List
class LinkedList:

    def __init__(self):
        self.head = None

    # Insertion
    def insertAtStart(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insertAtMiddle(self, prev_node, data):
        if self.head is None:
            print("Linked List is Empty.")
        else:
            node_required = self.head
            while node_required is not None:
                if node_required == prev_node:
                    temp_node = prev_node.next
                    prev_node.next = Node(data)
                    new_node = prev_node.next
                    new_node.next = temp_node
                    break
                node_required = node_required.next
            else:
                print("prev_node is not found.")

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data)

    # Deletion
    def deleteAtStart(self):
        if self.head is None:
            print("Head is pointing to None.")
        else:
            self.head = self.head.next

    def deleteAtMiddle(self, prev_node):
        if self.head is None:
            print("Linked List is Empty.")
        else:
            node_required = self.head
            while node_required is not None:
                if node_required == prev_node:
                    temp_node = prev_node.next
                    prev_node.next = temp_node.next
                    break
                node_required = node_required.next
            else:
                print("prev_node is not found.")

    def deleteAtEnd(self):
        if self.head is None:
            print("Head is pointing to None.")
        else:
            temp = self.head
            if temp.next is None:
                self.head = None
            else:
                next_temp = temp.next
                while next_temp.next is not None:
                    temp = next_temp
                    next_temp = temp.next
                temp.next = None

    # Searching
    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return f"{data} found"
            current = current.next
        return f"{data} not found"

    # Sorting
    def sortLinkedList(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            array = []
            while temp is not None:
                array.append(temp.data)
                array.sort()
                temp = temp.next
            self.head = Node(array[0])
            temp = self.head
            for i in range(1, len(array)):
                temp.next = Node(array[1])
                temp = temp.next

    # Printing
    def printLinkedList(self):
        temp = self.head
        array = []
        while temp is not None:
            array.append(temp.data)
            temp = temp.next
        print(array)


ll = LinkedList()
ll.insertAtEnd(1)
ll.insertAtStart(2)
ll.insertAtStart(3)
ll.insertAtEnd(4)
ll.insertAtMiddle(ll.head.next, 5)

print('linked list:')
ll.printLinkedList()

print("\nAfter deleting an element:")
ll.deleteAtEnd()
ll.deleteAtStart()
ll.deleteAtMiddle(ll.head)
ll.printLinkedList()

ll.sortLinkedList()
ll.printLinkedList()
print(ll.search(2))
print(ll.search(5))
