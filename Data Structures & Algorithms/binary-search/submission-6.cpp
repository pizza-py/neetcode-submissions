class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size()-1;
        int middle;
        while (left <= right){
            middle = ceil((left+right)/2);
            if (target < nums[middle]){
                right = middle-1;
            }
            else if (target > nums[middle]){
                left = middle + 1;
            }
            else if (target == nums[middle]){
                return middle;
            }
        }
        return -1;
    }
};
