class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int r = 1;
        int maxP = 0;
        while (r < prices.size()) {
            if (prices[l] < prices[r]) {
                int benefit = prices[r] - prices[l];
                maxP = benefit > maxP ? benefit : maxP;
            } else 
                l=r;
            r++;
        }

        return maxP;
    }
};
