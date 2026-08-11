class Solution:
    def findSum(self, s1, s2):

        i = len(s1) - 1
        j = len(s2) - 1

        carry = 0
        ans = []

        while i >= 0 or j >= 0 or carry:

            a = int(s1[i]) if i >= 0 else 0
            b = int(s2[j]) if j >= 0 else 0

            total = a + b + carry

            ans.append(str(total % 10))
            carry = total // 10

            i -= 1
            j -= 1

        result = ''.join(reversed(ans))

        # Remove leading zeros
        result = result.lstrip('0')

        # If everything was zero
        return result if result else "0"