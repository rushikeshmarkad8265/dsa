class Solution:
    def removeDuplicates(self, arr):
        # code here 
        i = 0
        j = 0
        result = []
        
        while (j<len(arr)):
            if arr[i]!=arr[j]:
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
                
            j+=1
        for j in range(i+1):
            result.append(arr[j])
        return result