class Solution:
    def countValidPrefixes(self, s: str) -> int:
        n = len(s)
        freq_map = {'0':0,'1':0}
        ans = 0
        for ch in s:
            freq_map[ch] = freq_map.get(ch)+1
            if freq_map['0']==freq_map['1']+1 or freq_map['1'] == freq_map['0']+1 or freq_map['0']==freq_map['1']:
                ans+=1
        return ans
            