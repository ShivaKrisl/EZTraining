# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = []
        dc=0
        # i=0
        # if k==1:
        #     for i in arr:
        #         if i>=threshold:
        #             dc+=1
        #     return dc
        # if len(arr)==100000 and k==50000:

        dc=0
        res.append(arr[0])
        cs = arr[0]
        size = 1
        i=0
        j = 1
        while j<len(arr):
            if size<k:
                # res.append(arr[j])
                cs+=arr[j]
                j+=1
                size+=1
            if size==k:
                if cs/k>=threshold:
                    dc+=1
                size-=1
                # j-=1
                # print(res)
                # res = res[1:]
                cs-=arr[i]
                i+=1
        return dc