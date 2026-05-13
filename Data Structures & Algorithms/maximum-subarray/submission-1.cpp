class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxP = nums[0];
        int maxT = 0;
        int i = 0;
        while (i < nums.size()) {
            if (maxT < 0) {
                maxT = nums[i];   
            } else {
                maxT = maxT + nums[i] > 0 ? maxT + nums[i] : nums[i];
            }

            maxP = maxT > maxP ? maxT : maxP;

            i++;
        }

        return maxP;
    }
};
