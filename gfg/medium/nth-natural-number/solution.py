class Solution:
    def findNth(self, n: int) -> str:
        # Step 1: Handle string inputs if necessary
        n = int(n)
    
        # Step 2: Convert base-10 integer n into a base-9 string
        result = []
        while n > 0:
            remainder = n % 9
            result.append(str(remainder))
            n = n // 9
    
        # Step 3: Reverse the list and join to form the final number string
        return "".join(reversed(result))
