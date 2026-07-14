class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        temp = ""
        # length = 0
        if len(s) == 1:
            return 1
        for i in range(len(s)-1):
            temp+=s[i]
            for j in range(i+1,len(s)):
                if s[j] in temp:
                    break
                temp += s[j]         
            ans = max(len(temp),ans)
            temp = ""
        
        return ans

        
