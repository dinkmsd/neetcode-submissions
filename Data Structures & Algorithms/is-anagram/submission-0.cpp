class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> mp;
        mp['c'] = 0;

        for (char i : s)
        {
            mp[i]++;
        }
        for (char i : t)
        {
            if (mp.find(i) == mp.end() || mp[i] == 0)
            {
                return false;
            }
            mp[i]--;
        }
        for (auto i : mp)
            if (i.second != 0)
                return false;
        return true;
    }
};
