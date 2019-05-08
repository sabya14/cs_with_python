MAX_SIZE = 10


class Stack:
    """
        Initialize the stacks with zero, we have to stacks.. one normal.. and one will have always
        have the min value in the top
    """
    def __init__(self):
        self.stack = [-1 for i in range(MAX_SIZE)]
        self.min_stack = [-1 for i in range(MAX_SIZE)]
        self.index = -1

    def is_full(self):
        """
        :return: if index == maxsize, means stack is full.. return true
        """
        if self.index == MAX_SIZE:
            return True

    def is_empty(self):
        """
        :return: if index is in -1, means stack is empty.. return true
        """
        if self.index == -1:
            return True
        else:
            return False

    def push(self, item):
        """
        :param item: item to pushed to stack
        :return: none
        """
        if self.is_full():
            return "Stack is Full"
        self.index = self.index + 1
        self.stack[self.index] = item
        # we check if item to pushed is less than the top of the min stack, if true then push else no
        if self.index is not 0:
            if self.min_stack[self.index - 1] > item:
                self.min_stack[self.index] = item
            else:
                self.min_stack[self.index] = self.min_stack[self.index - 1]
        else:
            self.min_stack[self.index] = item

    def pop(self):
        """
        :return: Return the last element pushed
        """
        if self.is_empty():
            return "Stack is empty"
        to_return = self.stack[self.index]
        self.stack[self.index] = 0
        self.min_stack[self.index] = 0
        self.index = self.index - 1
        return to_return

    def get_min(self):
        """
        :return: get the minimum element from the stack
        """
        return self.min_stack[self.index]


class Queue:

    def __init__(self):
        self.stack_a = Stack()
        self.stack_b = Stack()

    def push(self, data):
        if self.stack_a.is_empty() and not self.stack_b.is_empty():
            # reverse all element from stack b
            while not self.stack_b.is_empty():
                element = self.stack_b.pop()
                self.stack_a.push(element)
        self.stack_a.push(data)

    def pop(self):
        if self.stack_a.is_empty():
            if not self.stack_b.is_empty():
                return self.stack_b.pop()
            else:
                return "Cant pop"
        else:
            while not self.stack_a.is_empty():
                element = self.stack_a.pop()
                self.stack_b.push(element)

        return self.stack_b.pop()


q = Queue()
q.push(12)
q.push(1)
q.push(2)
q.push(3)
print(q.pop())
print(q.pop())
q.push(11)
q.push(33)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
