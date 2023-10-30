# https://leetcode.com/problems/design-a-stack-with-increment-operation/
class CustomStack:

    def __init__(self, maxSize: int):
        self.l = list()
        self.size = maxSize

    def push(self, x: int) -> None:
        if len(self.l)<self.size:
            self.l.append(x)

    def pop(self) -> int:
        if len(self.l):
            val = self.l.pop()
            return val
        return -1

    def increment(self, k: int, val: int) -> None:
        if len(self.l)<k:
            for i in range(len(self.l)):
                self.l[i]+=val
        else:
            for i in range(k):
                self.l[i]+=val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)