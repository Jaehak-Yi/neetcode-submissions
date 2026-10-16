class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = len(nums)
        left = 0
        right = L-1
        minimum = nums[0]
        
        while left <= right:
            if nums[left] < nums[right]:
                minimum = min(minimum, nums[left])
                break
            
            mid = left + (right - left) // 2
            minimum = min(minimum, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid -1
        
        return minimum
