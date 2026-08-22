class Solution:
    def longestConsecutive(self, arr):
        # code here
        st = set()
        n = len(arr)
        
        for val in arr:
            st.add(val)
        count = 0
        ans = float("-inf")
        for val in st:
            if val-1 not in st:
                temp = val
                while temp in st:
                    count+=1
                    temp+=1
                ans = max(ans,count)
                count = 0
        return ans