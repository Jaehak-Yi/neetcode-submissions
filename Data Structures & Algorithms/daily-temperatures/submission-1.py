class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        L = len(temperatures)
        result = [0]*L
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, ind = stack.pop()
                result[ind] = i - ind
            stack.append((t,i))
        return result