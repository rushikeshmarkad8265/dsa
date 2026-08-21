class Solution:
    def findMidSum(self, arr1, arr2):
        # code here
        i =0
        n = len(arr1)
        arr1 = arr1+arr2
        arr1.sort()
        return arr1[n-1]+arr1[n]