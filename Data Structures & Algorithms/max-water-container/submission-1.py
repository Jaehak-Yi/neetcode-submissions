class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = len(heights)
        maximum = 0
        left = 0
        right = L-1

        while left < right:
            area = min(heights[left],heights[right])*(right - left)
            if area > maximum:
                maximum = area
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maximum