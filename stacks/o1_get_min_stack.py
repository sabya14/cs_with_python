"""
 A stack   that will support all the stack operations like push(), pop(), isEmpty(), isFull()
 and an additional operation getMin() which should return minimum element from the stack.
 All should be done in linear time
"""
MAX_SIZE = 10


class Stack:
    """
        Initialize the stacks with zero, we have to stacks.. one normal.. and one will have always
        have the min value in the top
    """
    stack = [0 for i in range(MAX_SIZE)]
    min_stack = [0 for i in range(MAX_SIZE)]
    index = -1

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


# driver code
stack = Stack()
for item in [18, 19, 29, 15, 16]:
    stack.push(item)

print(stack.get_min())
print(stack.pop())
print(stack.pop())
print(stack.get_min())
