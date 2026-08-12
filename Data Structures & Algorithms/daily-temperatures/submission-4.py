class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)

        for i in range(len(temperatures)):
            if len(stack)==0:
                stack.append(i)
            
            elif temperatures[i]>=temperatures[stack[-1]]:
                while len(stack) and (temperatures[i]>temperatures[stack[-1]]):
                    index = stack[-1]
                    stack.pop()
                    result[index] = i - index
                
                stack.append(i)

            elif temperatures[i]<temperatures[stack[-1]]:
                stack.append(i)
            
    
        while len(stack):
            ind = stack.pop()
            result[ind]=0
        
        return result
            
