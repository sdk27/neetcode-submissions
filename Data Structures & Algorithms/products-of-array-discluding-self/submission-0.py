class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        product=1
        output=[]
        icount=nums.count(0)
        for i in range(length):
            if icount==0:
                product*=nums[i]
            elif icount==1:
                if nums[i]!=0:
                    product*=nums[i]
            
        for j in range(length):
            if icount==0:
                output.append(product//nums[j])
            elif icount==1:
                if nums[j]!=0:
                    output.append(0)
                else:
                    output.append(product)
            else:
                output.append(0)
        return output

        

         