class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min_stack.append(val)
        else:
            min_val = min(self.min_stack[-1], val)
            self.min_stack.append(min_val)
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
