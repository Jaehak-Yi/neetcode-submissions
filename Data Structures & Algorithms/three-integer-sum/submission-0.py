class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        L = len(nums)
        for first in range(L-2):
            if nums[first] > 0:
                break

            elif nums[first] == nums[first -1] and first > 0:
                continue

            second = first + 1
            last = L-1
            while second < last:
                sums = nums[first] + nums[second] + nums[last]
                if sums == 0:
                    answer.append([nums[first], nums[second], nums[last]])
                    while second < last and nums[last] == nums[last-1]:
                        last -= 1
                    while second < last and nums[second] == nums[second+1]:
                        second += 1
                    second += 1
                elif sums > 0:
                    last -= 1
                elif sums < 0:
                    second += 1
        return answer