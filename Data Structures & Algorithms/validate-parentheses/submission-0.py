class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[" or len(stack) == 0:
                stack = [i]+stack
            if i == ")":
                if stack[0] == "(":
                    stack = stack[1:]
                else:
                    return False
            elif i == "}":
                if stack[0] == "{":
                    stack = stack[1:]
                else:
                    return False
            elif i == "]":
                if stack[0] == "[":
                    stack = stack[1:]
                else:
                    return False
        if len(stack) != 0:
            return False
        else:
            return True
                    
