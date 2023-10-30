# https://leetcode.com/problems/implement-queue-using-stacks/
class MyQueue:

    def __init__(self):
        self.l = list()

    def push(self, x: int) -> None:
        self.l.append(x)

    def pop(self) -> int:
        val = self.l[0]
        del self.l[0]
        return val
    def peek(self) -> int:
        return  self.l[0]

    def empty(self) -> bool:
        return True if len(self.l)==0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()