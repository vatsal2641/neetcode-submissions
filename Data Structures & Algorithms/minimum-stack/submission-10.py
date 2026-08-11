class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = float('inf')


    def push(self, val: int) -> None:
       
        if self.mini>val:
            self.mini = val
            
        self.stack.append(val)
        

    def pop(self) -> None:
        if len(self.stack):
            self.stack.pop()
       
            if len(self.stack):
                self.mini = min(self.stack)
            else:
                self.mini = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini
