class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = [] 

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.min_stk or val <= self.min_stk[-1]:
            self.min_stk.append(val)
        #최소이거나 최소랑 같거나 추가 


    def pop(self) -> None:
        val = self.stk.pop()
        if self.min_stk and val == self.min_stk[-1]:
            self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1] if self.stk else None
        

    def getMin(self) -> int:
        return self.min_stk[-1] if self.min_stk else None

        
