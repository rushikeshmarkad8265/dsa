class Solution:
    def nextLargerElement(self, arr):
        # code here
        ng = [-1]*len(arr)
        index = []
        n = len(arr)
        for i in range(n-1,-1,-1):
            
            while index and arr[index[-1]] <= arr[i]:
                index.pop()
            
            if not index:
                ng[i] = -1
            else :
                ng [i] = arr[index[-1]]
            
            index.append(i)
            
        
        return ng