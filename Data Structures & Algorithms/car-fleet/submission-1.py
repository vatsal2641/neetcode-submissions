class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        time = []

        speed = [s for p,s in sorted(zip(position, speed), reverse=True)]
        position.sort(reverse=True)
        

        for i in range(n):
            time.append((target - position[i])/speed[i])
        
        fleet_count = 0
        stack = []

        for i in range(n):
            if len(stack) == 0:
                stack.append(time[i])
            
            elif stack[0]>=time[i]:
                continue
            
            else:
                while len(stack):
                    stack.pop() 
                fleet_count+=1
                stack.append(time[i])
        
        if len(stack):                   # Last fleet
            fleet_count+=1


        return fleet_count
