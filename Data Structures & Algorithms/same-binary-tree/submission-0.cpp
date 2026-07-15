/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<int> dfs(TreeNode*root){
        if (root == nullptr){
            return {101};
        } else {
            vector<int> v1 = dfs(root->left);
            vector<int> v2 = dfs(root->right);
            vector<int> v3 = {root->val};
            for (int i=0; i<v1.size();i++){
                v3.push_back(v1[i]);
            }
            for (int i=0; i<v2.size();i++){
                v3.push_back(v2[i]);
            }
            return v3;
        }
    }
    bool isSameTree(TreeNode* p, TreeNode* q) {
        return (dfs(p) == dfs(q));
    }
};
