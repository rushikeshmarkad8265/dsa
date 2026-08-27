class Solution:
    def countPairs(self, arr: list[int], k: int) -> int:
        arr.sort()
        count = 0
        j = 0
        n = len(arr)
    
        for i in range(n):
            # Move j forward until the difference is no longer less than k
            while j < n and arr[j] - arr[i] < k:
                j += 1
            # All elements from i+1 to j-1 are valid pairs with i
            count += (j - 1 - i)
    
        return count
