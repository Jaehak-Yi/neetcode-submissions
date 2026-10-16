class Solution:
    def trap(self, height: List[int]) -> int:
        L = len(height)
        ans = 0
        left = 0
        right = L-1
        leftmax = height[left]
        rightmax = height[right]

        while left < right:
            if leftmax < rightmax:
                left += 1
                leftmax = max(leftmax, height[left])
                ans += leftmax-height[left]      
            else:
                right -= 1
                rightmax = max(rightmax, height[right])
                ans += rightmax - height[right]
        return ans  