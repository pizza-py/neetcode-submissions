class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> newList;
        for (int i=0;i<2*nums.size();i++){
            newList.push_back(nums.at(i%nums.size()));
        }
        return newList;
    }
};