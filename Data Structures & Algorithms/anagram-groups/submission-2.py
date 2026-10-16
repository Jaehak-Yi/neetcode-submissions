class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictstr = {}
        answer = []
        for i in strs:
            temp = "".join(sorted(i))
            if temp not in dictstr:
                dictstr[temp] = [i]
            else:
                dictstr[temp].append(i)
        for i in dictstr.values():
            answer.append(i)
        return answer
        
            