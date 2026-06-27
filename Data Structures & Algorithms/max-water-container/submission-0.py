class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum =0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                width = j-i
                h = min(heights[i],heights[j])
                area = width * h
                maximum = max(area,maximum)
        return maximum
        