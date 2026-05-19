import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        length=len(nums)
        for i in range(length):
            l1=nums[:i]
            l2=nums[i+1:]
            if len(l1)>0:
                p1=math.prod(l1)
            else:
                p1=1
            if len(l2)>0:
                p2=math.prod(l2)
            else:
                p2=1
            output.append(p1*p2)
        return output


