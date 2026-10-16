class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            encoded_string += str(len(i))
            encoded_string += "*"
            encoded_string += i
        return encoded_string

    def decode(self, s: str) -> List[str]:
        nums = ["1", "2", "3", "4", "5", "6","7","8","9","0"]
        L = list(s)
        decoded_strs = []

        while len(L) > 0:
            length = 0
            i = 0
            while L[i] in nums:
                length = length*10 + int(L[i])
                i = i+1
            L = L[i+1:]
            decoded_strs.append("".join(L[:length]))
            L = L[length:]
        return decoded_strs
        


