class Solution {
public:
    int missingNumber(vector<int>& arr) {
        sort(arr.begin(), arr.end());

        int target = 1;
        for (int num : arr) {
            if (num == target) {
                target++;
            }
        }

        return target;
    }
};