
class Stack(object):
    """
    Stack is initailized for myself

    """
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    stack = Stack()

    stack.push(1)

    print stack.size()
    print stack.peek()

    for x in range(20):
        stack.push(x)

    while not stack.isEmpty():
        print stack.pop()
