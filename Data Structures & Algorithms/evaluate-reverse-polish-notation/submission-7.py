import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator_lookup={
            "+": operator.add, 
            "-": operator.sub, 
            "*": operator.mul, 
            "/": operator.truediv
        }

        for c in tokens:
   
            if c.isdigit() or (c.startswith('-') and c[1:].isdigit()):
                stack.append(int(c))
    
            else:
                op2= stack.pop()
                op1= stack.pop()
                op = operator_lookup[c]
                ans = op(op1, op2)
                stack.append(int(ans))
        return stack[-1]
