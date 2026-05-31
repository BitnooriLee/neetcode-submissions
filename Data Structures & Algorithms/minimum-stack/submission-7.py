class MinStack:

    def __init__(self):
        self.stk = []
        self.current_min = []

    def push(self, val: int) -> None:
        if self.stk:
            cur_min = self.getMin()
            self.current_min.append(min(cur_min, val))
        else:
            self.current_min.append(val)
        self.stk.append(val)
    def pop(self) -> None:
        self.stk.pop()
        self.current_min.pop()

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.current_min[-1]

        
