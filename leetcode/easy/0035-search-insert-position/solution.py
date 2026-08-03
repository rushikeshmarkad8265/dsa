class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = len(nums)
        start = 0
        end = len(nums)-1
        if target < nums[0]:
            return 0
        while start <= end:
            mid = (start + end)//2
            if nums[mid]>=target:
                ans = mid
                end = mid-1
            else:             
                start = mid+1
        
        return ans
