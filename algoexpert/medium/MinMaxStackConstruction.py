# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.minmaxstack = []
        self.stack = []

    def peek(self):
        if self.isStackEmpty():
            raise IndexError('peek from an empty stack')
        return self.stack[-1]

    def pop(self):
        if self.isStackEmpty():
            raise IndexError('peek from an empty stack')
        self.minmaxstack.pop()
        return self.stack.pop()

    def push(self, number):
        minimum = min(self.getMin(), number) if not self.isStackEmpty() else number
        maximum = max(self.getMax(), number) if not self.isStackEmpty() else number
        self.minmaxstack.append([minimum, maximum])
        self.stack.append(number)

    def getMin(self):
        if self.isStackEmpty():
            raise IndexError('getMin from an empty stack')
        return self.minmaxstack[-1][0]

    def getMax(self):
        if self.isStackEmpty():
            raise IndexError('getMax from an empty stack')
        return self.minmaxstack[-1][1]

    def isStackEmpty(self):
        return len(self.stack) == 0
