class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> umap;
        for (auto i : nums) {
            if (umap[i]) return true;
            umap[i]++;
        }
        return false;
    }
};
