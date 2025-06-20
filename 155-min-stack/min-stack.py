class MinStack:

    def __init__(self):
        self.st = []
        self.mini = 0

    def push(self, val: int) -> None:
        if len(self.st)==0:
            self.st.append(val)
            self.mini = val
        elif val<self.mini:
            self.st.append(2*val-self.mini)
            self.mini=val
        else:
            self.st.append(val)
        # print(self.st,self.mini)

    def pop(self) -> None:
        if self.st[-1]<self.mini:
            self.mini = 2*self.mini-self.st[-1]
        self.st.pop()
        # print(self.st,self.mini)

    def top(self) -> int:
        # print(self.st,self.mini)
        if self.st[-1]<self.mini:
            return self.mini
        else:
            return self.st[-1]
        

    def getMin(self) -> int:
        # print(self.st,self.mini)
        return self.mini



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()