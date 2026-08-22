class Solution:
    def twoRepeated(self, arr):
        # code here
        
        my_freq = {}
        ans = []
        for num in arr:
            my_freq[num] = my_freq.get(num,0)+1
            if my_freq[num]>1:
                ans.append(num)
        
        return ans