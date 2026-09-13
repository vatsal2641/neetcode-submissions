class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)   #For this course this is the prerequisite. 

        # A course has 3 possible states:
        #visited - crs has been added to the output.
        #visiting - crs has not been added to output, but added to the cycle.
        #unvisited-neither to the output nor to the cycle. 

        output = []
        visit, cycle = set(), set()

        def dfs(crs):

            if crs in cycle:
                return False
            
            if crs in visit: 
                return True     #Anything else then True can also be returned

            cycle.add(crs)

            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False   # cycle detected

            cycle.remove(crs)   # No active cycle under this node. 
            visit.add(crs)      
            output.append(crs)

            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return output
        