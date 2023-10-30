# https://leetcode.com/problems/baseball-game/
class Solution:
    def calPoints(self, op: List[str]) -> int:
        l = []
        for i in range(len(op)):
            if op[i] == 'C':
                if len(l)>0:
                    l.pop()
            elif op[i]=='D':
                l.append(2*l[-1])
            elif op[i]=='+':
                l.append(l[-1]+l[-2])
            else:
                l.append(int(op[i]))
                print(l)
        return sum(l)