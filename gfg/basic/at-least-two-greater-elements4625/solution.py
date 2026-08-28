class Solution:
    def findElements(self,arr):
        # code here
        arr.sort()
        return arr[:len(arr)-2]
