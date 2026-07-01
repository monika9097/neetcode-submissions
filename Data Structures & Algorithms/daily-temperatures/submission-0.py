class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[0]
        res =[0] * len(temperatures)
        for t in range(1,len(temperatures)):
            while stack and temperatures[t] > temperatures[stack[-1]]:
                prev = stack.pop()
                day = t-prev
                res[prev] = day
            stack.append(t)
        return res
       
                


        