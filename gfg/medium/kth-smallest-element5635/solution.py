class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        arr.sort()
        a = k -1
       
        return arr[a]
