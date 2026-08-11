class Solution:
    def is_matching(self, s1: str, s2: str) -> bool:
        if (s1 == "(" and s2==")") or (s1 == "[" and s2=="]") or (s1 == "{" and s2=="}"):
            return True
        return False

    def isValid(self, s: str) -> bool:
        bracket_set = set(["(", "[", "{"])
        stack = []
        for c in s:
            if c in bracket_set:
                stack.append(c)
            else:
                if len(stack) and self.is_matching(stack[-1], c):
                    stack.pop()
                else:
                    return False
        
        if len(stack):
            return False
        return True
