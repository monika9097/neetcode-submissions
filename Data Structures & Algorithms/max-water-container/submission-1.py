class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum =0
        i,j=0,len(heights)-1
        while i<j:
            maximum = max(maximum,min(heights[j],heights[i])*(j-i))
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return maximum
            

        