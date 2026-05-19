class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {} 
        
        for  i in nums:
            if i in count:
                count[i] += 1
                if count[i] > 1:
                    return True
            else:
                count[i] = 1
        
        return False