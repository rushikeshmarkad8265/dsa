class Solution:
    def sortSentence(self, s: str) -> str:
        str_list = s.split()
        result = [""]*len(str_list)

        for word in str_list:
            n = len(word)-1
            pos = int(word[n])

            result[pos-1] = word[:n]

        return str(result)
