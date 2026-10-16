class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        HashTable = {}
        for i in nums:
            if i not in HashTable:
                HashTable[i] = 1
            else:
                HashTable[i] += 1
        answer = []
        for i in range(k):
            max = 0
            index = 0
            for j in HashTable:
                if HashTable[j] > max:
                    index = j
                    max = HashTable[j]
            answer.append(index)
            HashTable[index] = -1
        return answer