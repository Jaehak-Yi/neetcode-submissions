class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        prod = 1
        numofzero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                prod = prod*nums[i]
            else:
                numofzero += 1
        if numofzero > 1 :
            return [0]*len(nums)
        
        for i in range(len(nums)):
            if nums[i] != 0 and numofzero == 1:
                answer.append(0)
            elif numofzero == 1:
                answer.append(prod)
            else:
                answer.append(int(prod/nums[i]))
        return answer