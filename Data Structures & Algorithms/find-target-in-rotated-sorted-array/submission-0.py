class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,h=0,len(nums)-1
        while l<=h:
            mid=(l+h)//2
            if nums[mid]==target:
                return mid
            elif nums[l]<= nums[mid]:
                if nums[l]<=target<nums[mid]:
                    h=mid-1 #move left
                else:
                    l=mid+1 #move right
            else:
                if nums[mid]< target<=nums[h]:
                    l=mid+1   #move right
                else:
                    h=mid-1  #move left
        return -1
