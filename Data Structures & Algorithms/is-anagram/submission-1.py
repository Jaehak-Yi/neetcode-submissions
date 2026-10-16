class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = []

        for i in s:
            if i not in seen:
                seen.append(i)
        sdict = dict(zip(seen, [0]*len(seen)))

        for i in s:
            sdict[i] += 1
        
        for i in t:
            if i not in seen:
                return False
            else:
                sdict[i] -= 1
                if sdict[i] < 0:
                    return False
        for i in range(len(seen)):
            if sdict[seen[i]] != 0:
                return False
        return True