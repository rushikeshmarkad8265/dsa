class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num,0)+1
        
        count = 0
        for num in freq_map:
            if freq_map[num]>2:
                count+=2
            else:
                count+=freq_map[num]
        
        return count