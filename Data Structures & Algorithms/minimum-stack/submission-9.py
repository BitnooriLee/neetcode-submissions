class MinStack:

    def __init__(self):
        self.stk = []
        self.m_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if self.m_stk and self.m_stk[-1] < val:
            self.m_stk.append(self.m_stk[-1])
        else:
            self.m_stk.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.m_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.m_stk[-1]

        
