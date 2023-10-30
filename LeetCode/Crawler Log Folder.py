#  https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        l = []
        for i in logs:
            if i=='./':
                continue
            elif i=='../':
                if len(l)>0:
                    l.pop()
                else:
                    continue
            else:
                l.append(i)
        return len(l)