class Solution:
    def kthElement(self, a, b, k):
        # code here
        a = a + b
        a.sort()
        return a[k-1]