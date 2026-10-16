class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation = ["+", "-", "*", "/"]
        number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        stack = []
        
        for i in tokens:
            if i not in operation:
                stack.append(int(i))
            elif i == "+":
                b, a = stack.pop(), stack.pop()
                stack.append(a + b)
            elif i == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif i == "*":
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)
            elif i == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
        return stack[0]