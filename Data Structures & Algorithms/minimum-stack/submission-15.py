class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = float('inf')


    def push(self, val: int) -> None:
        if len(self.stack)==0:
            self.mini = val

        self.stack.append(val-self.mini)    
        
        if self.mini>val:
            self.mini = val

    def pop(self) -> None:
        if self.stack[-1]<=0:
            self.mini = self.mini - self.stack[-1]

        self.stack.pop()


    def top(self) -> int:
        if self.stack[-1]<0:
            return self.mini
        return self.stack[-1]+ self.mini

    def getMin(self) -> int:
        return self.mini
       
