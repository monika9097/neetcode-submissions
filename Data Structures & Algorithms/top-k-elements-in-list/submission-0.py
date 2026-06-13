class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        output =[]
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i]=1
        freq = list(count.items())
        freq.sort(key=lambda x: x[1],reverse =True)

        output = [num for num, value in freq[:k]]
       

        return output
