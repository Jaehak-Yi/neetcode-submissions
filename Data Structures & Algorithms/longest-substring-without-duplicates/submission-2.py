class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slist = list(s)
        L = len(slist)
        if L == 0:
            return 0
        if L == 1:
            return 1

        left = 0
        seen = set()

        res = 1

        for right in range(L):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            res = max(res, right - left + 1)
        return res
