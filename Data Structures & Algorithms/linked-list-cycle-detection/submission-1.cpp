/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    bool hasCycle(ListNode* head) {
        ListNode* cur = head;
        vector<ListNode*> seen;

        while (cur != nullptr){
            for (int i=0; i<seen.size(); i++){
                if (seen[i] == cur){
                    return true;
                }
            }
            seen.push_back(cur);
            cur = cur->next;
        }

        return false;
    }
};
