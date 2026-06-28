class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n==0: return 0
        leftmax=[0]*n
        leftmax[0] =height[0]
        rightmax=[0]*n
        rightmax[n-1] = height[n-1]
        water =0

        for i in range(1,n):
            leftmax[i] = max(height[i],leftmax[i-1])
        for i in range(n-2,-1,-1):
            rightmax[i]= max(rightmax[i+1],height[i])
        for i in range(0,n):
            water += min(leftmax[i],rightmax[i]) -height[i]
        return water
        
        