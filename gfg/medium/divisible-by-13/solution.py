class Solution:
    def divby13(self, s: str) -> int:
        # Step 1: Initialize the running remainder
        remainder = 0
    
        # Step 2: Process each character digit-by-digit
        for char in s:
            # Update the remainder using math: (remainder * 10 + current_digit) % 13
            remainder = (remainder * 10 + int(char)) % 13
    
        # Step 3: Return 1 if perfectly divisible (remainder is 0), otherwise 0
        return 1 if remainder == 0 else 0
