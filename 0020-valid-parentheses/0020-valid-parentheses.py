class Solution:
    def isMatched(self, open, close):
        if ((open == '(' and close == ')') or (open == '[' and close == ']') or (open == '{' and close == '}')):
            return True
        return False

    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                ch = stack[-1]
                stack.pop()
                if not self.isMatched(ch, s[i]):
                    return False
        return not stack
         