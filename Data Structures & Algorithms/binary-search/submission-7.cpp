class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size()-1;
        while (left <= right){
            int index = ceil((left + right)/2);
            if (nums.at(index) == target){
                return index;
            } else if (nums.at(index) < target){
                left = index + 1;
            } else {
                right = index - 1;
            }
        }

        return -1;
    }
};
