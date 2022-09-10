class Stack:

    def __init__(self):
        self.stack = []

    # Push
    def push(self, element):
        self.stack.append(element)

    # Pop
    def pop(self):
        if len(self.stack) < 1:
            return "Stack is empty"
        return self.stack.pop()


s = Stack()
print(s.pop())
s.push(1)
s.push(2)
s.push(3)
print(s.stack)
print(s.pop())
print(s.stack)
