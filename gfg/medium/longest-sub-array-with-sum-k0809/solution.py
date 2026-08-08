class Solution:
    def longestSubarray(self, arr, k):

        prefix_sum = 0
        first_index = {}

        ans = 0

        for i in range(len(arr)):

            prefix_sum += arr[i]

            # Subarray starts from index 0
            if prefix_sum == k:
                ans = i + 1

            # Check if a previous prefix exists
            if prefix_sum - k in first_index:
                length = i - first_index[prefix_sum - k]
                ans = max(ans, length)

            # Store FIRST occurrence only
            if prefix_sum not in first_index:
                first_index[prefix_sum] = i

        return ans