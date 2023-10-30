# https://leetcode.com/problems/pascals-triangle-ii/
from math import factorial as f
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        l = []
        for i in range(rowIndex+1):
            x = []
            for j in range(i+1):
                x.append((f(i)//(f(i-j)*f(j))))
            l.append(x)
        return l[rowIndex]
