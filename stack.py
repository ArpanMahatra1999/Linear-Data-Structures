# create stack
def create_stack():
    stack = []
    return stack


# check if stack is empty
def is_empty(stack):
    if len(stack) == 0:
        return True
    return False


# pushing an element into stack
def push(stack, element):
    stack.append(element)
    return stack


# popping an element from stack
def pop(stack):
    if is_empty(stack):
        return "Stack is empty"
    return stack.pop()


my_stack = create_stack()
print(pop(my_stack))
push(my_stack, 1)
push(my_stack, 2)
push(my_stack, 3)
print(my_stack)
print(pop(my_stack))
print(my_stack)
