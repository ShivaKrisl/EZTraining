# https://leetcode.com/problems/search-a-2d-matrix-ii/
class Solution:
    def BS(self,l,target):
        start = 0
        end = len(l)-1
        while start<=end:
            mid = start+(end-start)//2
            if l[mid]==target:
                return True
            elif l[mid]>target:
                end = mid-1
            else:
                start = mid+1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target<=matrix[i][-1]:
                ans = self.BS(matrix[i],target)
                if ans==True:
                    return ans
        return False