class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stackl = []
        count_l = [0]*len(heights)
        n = len(heights)
        for i in range(n):
            if len(stackl)==0:
                stackl.append(i)
                count_l[i] = 0
            
            else:
                if heights[i] >  heights[stackl[-1]]:
                    stackl.append(i)
                    count_l[i] = 0
                else:
                    count_i_val = 0
                    while len(stackl) and heights[i] <=  heights[stackl[-1]]:
                        removed_idx = stackl.pop()
                        count_i_val += count_l[removed_idx]     #For the count of element
                        count_i_val +=1    #For poping the element itself
                    stackl.append(i)
                    count_l[i] = count_i_val
        
        stackr = []
        count_r = [0]*len(heights)
        for i in range(n-1,-1,-1):
            if len(stackr)==0:
                stackr.append(i)
                count_r[i] = 0

            else: 
                if heights[i] >  heights[stackr[-1]]:
                    stackr.append(i)
                    count_r[i] = 0
                else:
                    count_i_val = 0
                    while len(stackr) and heights[i] <=  heights[stackr[-1]]:
                        removed_idx = stackr.pop()
                        count_i_val += count_r[removed_idx] 
                        count_i_val +=1
                    stackr.append(i)
                    count_r[i] = count_i_val

        max_area = 0
        curr_area = 0
     
        for i in range(n):
            curr_area = (count_l[i] + count_r[i] + 1)*heights[i]
            max_area = max(max_area, curr_area)

        return max_area