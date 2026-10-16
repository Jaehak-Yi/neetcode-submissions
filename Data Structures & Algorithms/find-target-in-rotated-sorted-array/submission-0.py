class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = len(nums)
        left = 0
        right = L-1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] < nums[right]:
                    if nums[mid] <= target and target <= nums[right]:
                        left = mid
                    else:
                        right = mid
                elif nums[mid] > nums[right]:
                    if target >= nums[mid] or target <= nums[right]:
                        left = mid
                    else:
                        right = mid
            if abs(left - right) <= 1:
                if nums[left] == target:
                    return left
                elif nums[right] == target:
                    return right
                else:
                    return -1