class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = ''
        temp = s[0]
        for i in range(len(s)-1):           
            if ord(s[i])==ord(s[i+1])-1:
                temp+=s[i+1]
            
            else :
                if len(ans)<len(temp):
                    ans=temp
                temp = s[i+1]
        if len(ans)<len(temp):
             ans=temp

        return len(ans)