class MinStack:

    def __init__(self):
        self.stk = []
        self.minst = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if self.minst and val > self.getMin():
            self.minst.append(self.getMin())
        else:
            self.minst.append(val)

    def pop(self) -> None:
        if self.stk:
            self.stk.pop()
            self.minst.pop()

    def top(self) -> int:
        if self.stk:
            return self.stk[-1]
        

    def getMin(self) -> int:
        if self.minst:
            return self.minst[-1]
        
